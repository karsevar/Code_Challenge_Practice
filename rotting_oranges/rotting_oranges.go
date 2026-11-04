func orangesRotting(grid [][]int) int {
	visited := map[[2]int]bool{}
	totalOranges := 0
	queue := [][3]int{}

	for j := 0; j < len(grid); j++ {
		for i := 0; i < len(grid[0]); i++ {
			if grid[j][i] == 2 {
				queue = append(queue, [3]int{0, j, i})
				visited[[2]int{j, i}] = true
				totalOranges += 1
			} else if grid[j][i] == 1 {
				totalOranges += 1
			}
		}
	}

	total_minutes := 0

	for len(queue) > 0 {
		current_element := queue[0]
		queue = queue[1:]

		if total_minutes < current_element[0] {
			total_minutes = current_element[0]
		}

		for _, neighbor := range find_neighbors(current_element[1], current_element[2], grid) {
			if _, exists := visited[neighbor]; exists != true && grid[neighbor[0]][neighbor[1]] == 1 {
				queue = append(queue, [3]int{current_element[0] + 1, neighbor[0], neighbor[1]})
				visited[[2]int{neighbor[0], neighbor[1]}] = true
			}
		}
	}

	if totalOranges == len(visited) {
		return total_minutes
	}

	return -1
}

func find_neighbors(j int, i int, grid [][]int) [][2]int {
	neighbors := [][2]int{}

	if j < len(grid)-1 {
		neighbors = append(neighbors, [2]int{j + 1, i})
	}
	if i < len(grid[0])-1 {
		neighbors = append(neighbors, [2]int{j, i + 1})
	}
	if j > 0 {
		neighbors = append(neighbors, [2]int{j - 1, i})
	}
	if i > 0 {
		neighbors = append(neighbors, [2]int{j, i - 1})
	}

	return neighbors
}