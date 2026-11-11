func findMaxFish(grid [][]int) int {
	maxCount := 0
	visited := map[[2]int]bool{}

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if _, exists := visited[[2]int{i, j}]; exists != true && grid[i][j] != 0 {
				queue := [][2]int{}
				queue = append(queue, [2]int{i, j})
				visited[[2]int{i, j}] = true
				currentCount := grid[i][j]

				for len(queue) > 0 {
					currentCell := queue[0]
					queue = queue[1:]

					for _, neighbor := range findNeighbors(currentCell, grid) {
						if _, exists := visited[neighbor]; exists != true && grid[neighbor[0]][neighbor[1]] != 0 {
							queue = append(queue, neighbor)
							visited[neighbor] = true
							currentCount += grid[neighbor[0]][neighbor[1]]
						}
					}
				}

				if maxCount < currentCount {
					maxCount = currentCount
				}
			}
		}
	}
	return maxCount

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