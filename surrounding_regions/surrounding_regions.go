func solve(board [][]byte) {
	for j := 0; j < len(board); j++ {
		for i := 0; i < len(board[0]); i++ {
			if string(board[j][i]) == "O" {
				currentCell := [2]int{j, i}
				visited := map[[2]int]bool{}
				visited[currentCell] = true
				dfs(
					currentCell,
					board,
					&visited,
				)

				convert := true
				for cell, _ := range visited {
					if cell[0] == 0 || cell[1] == 0 || cell[0] == len(board)-1 || cell[1] == len(board[0])-1 {
						convert = false
					}
				}

				if convert {
					for cell, _ := range visited {
						board[cell[0]][cell[1]] = 'X'
					}
				}
			}
		}
	}
}

func dfs(currentCell [2]int, board [][]byte, results *map[[2]int]bool) {
	for _, neighbor := range findNeighbors(currentCell, board) {
		if _, exists := (*results)[neighbor]; string(board[neighbor[0]][neighbor[1]]) == "O" && exists == false {
			(*results)[neighbor] = true
			dfs(
				neighbor,
				board,
				results,
			)
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