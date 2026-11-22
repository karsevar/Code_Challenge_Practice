func updateMatrix(mat [][]int) [][]int {
	rows := len(mat)
	cols := len(mat[0])

	queue := [][2]int{}

	distances := make([][]int, rows)
	for i := range distances {
		distances[i] = make([]int, cols)
		for j := range distances[i] {
			distances[i][j] = -1
		}
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if mat[i][j] == 0 {
				queue = append(queue, [2]int{i, j})
				distances[i][j] = 0
			}
		}
	}

	for len(queue) > 0 {
		current_indexes := queue[0]
		queue = queue[1:]

		for _, neighbor := range findNeighbors(current_indexes[0], current_indexes[1], rows, cols) {
			if distances[neighbor[0]][neighbor[1]] == -1 {
				distances[neighbor[0]][neighbor[1]] = distances[current_indexes[0]][current_indexes[1]] + 1
				queue = append(queue, [2]int{neighbor[0], neighbor[1]})
			}
		}
	}
	return distances
}

func findNeighbors(i int, j int, rows int, cols int) [][2]int {
	neighbors := [][2]int{}

	if i > 0 {
		neighbors = append(neighbors, [2]int{i - 1, j})
	}
	if j > 0 {
		neighbors = append(neighbors, [2]int{i, j - 1})
	}
	if i < rows-1 {
		neighbors = append(neighbors, [2]int{i + 1, j})
	}
	if j < cols-1 {
		neighbors = append(neighbors, [2]int{i, j + 1})
	}
	return neighbors
}