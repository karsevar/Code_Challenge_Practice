func maxAreaOfIsland(grid [][]int) int {
	visited := map[[2]int]bool{}
	maxArea := 0

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if _, exists := visited[[2]int{i, j}]; grid[i][j] == 1 && exists != true {
				stack := [][2]int{}
				stack = append(stack, [2]int{i, j})
				currentArea := 1
				visited[[2]int{i, j}] = true

				for len(stack) > 0 {
					currentCell := stack[len(stack)-1]
					stack = stack[:len(stack)-1]

					for _, neighbor := range findNeighbors(currentCell, grid) {
						if _, exists := visited[[2]int{neighbor[0], neighbor[1]}]; exists == false && grid[neighbor[0]][neighbor[1]] == 1 {
							stack = append(stack, neighbor)
							visited[[2]int{neighbor[0], neighbor[1]}] = true
							currentArea += 1
						}
					}
				}

				if currentArea > maxArea {
					maxArea = currentArea
				}
			}
		}
	}

	return maxArea
}

func findNeighbors(currentCell [2]int, grid [][]int) [][2]int {
	neighbors := [][2]int{}
	if currentCell[0] > 0 {
		neighbors = append(neighbors, [2]int{currentCell[0] - 1, currentCell[1]})
	}
	if currentCell[1] > 0 {
		neighbors = append(neighbors, [2]int{currentCell[0], currentCell[1] - 1})
	}
	if currentCell[0] < len(grid)-1 {
		neighbors = append(neighbors, [2]int{currentCell[0] + 1, currentCell[1]})
	}
	if currentCell[1] < len(grid[0])-1 {
		neighbors = append(neighbors, [2]int{currentCell[0], currentCell[1] + 1})
	}
	return neighbors
}