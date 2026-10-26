func exist(board [][]byte, word string) bool {
	for j := 0; j < len(board); j++ {
		for i := 0; i < len(board[0]); i++ {
			if board[j][i] == word[0] {
				results := [][]byte{}
				visited := map[[2]int]bool{}
				visited[[2]int{j, i}] = true
				recursionHelper(
					[]byte{board[j][i]},
					word[1:],
					[2]int{j, i},
					board,
					&results,
					visited,
				)

				if len(results) > 0 {
					return true
				}
			}
		}
	}

	return false
}

func recursionHelper(state []byte, word string, currentCell [2]int, board [][]byte, results *[][]byte, visited map[[2]int]bool) {
	if len(word) == 0 {
		copiedState := append([]byte(nil), state...)
		*results = append(*results, copiedState)
	}

	if len(word) > 0 {
		neighbors := findNeighbors(currentCell, board)

		for _, neighbor := range neighbors {
			if _, exists := visited[neighbor]; board[neighbor[0]][neighbor[1]] == word[0] && exists != true {
				state = append(state, board[neighbor[0]][neighbor[1]])
				visited[neighbor] = true
				recursionHelper(
					state,
					word[1:],
					neighbor,
					board,
					results,
					visited,
				)

				state = state[:len(state)-1]
				delete(visited, neighbor)
			}
		}
	}
}

func findNeighbors(currentCell [2]int, board [][]byte) [][2]int {
	neighbors := [][2]int{}

	if currentCell[0] > 0 {
		neighbors = append(neighbors, [2]int{currentCell[0] - 1, currentCell[1]})
	}

	if currentCell[0] < len(board)-1 {
		neighbors = append(neighbors, [2]int{currentCell[0] + 1, currentCell[1]})
	}

	if currentCell[1] > 0 {
		neighbors = append(neighbors, [2]int{currentCell[0], currentCell[1] - 1})
	}

	if currentCell[1] < len(board[0])-1 {
		neighbors = append(neighbors, [2]int{currentCell[0], currentCell[1] + 1})
	}

	return neighbors
}