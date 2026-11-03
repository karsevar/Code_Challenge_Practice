func countBattleships(board [][]byte) int {
	visited := map[[2]int]bool{}
	shipCount := 0

	for j := 0; j < len(board); j++ {
		for i := 0; i < len(board[0]); i++ {
			currentIndexes := [2]int{j, i}
			if _, exists := visited[currentIndexes]; exists == false && string(board[j][i]) == "X" {
				visited[currentIndexes] = true
				recursionHelper(currentIndexes, board, visited)
				shipCount += 1
			}
		}
	}
	return shipCount
}

func recursionHelper(currentIndex [2]int, board [][]byte, visited map[[2]int]bool) {
	for _, neighbor := range findNeighbors(currentIndex, board) {
		if _, exists := visited[neighbor]; exists == false && string(board[neighbor[0]][neighbor[1]]) == "X" {
			visited[neighbor] = true
			recursionHelper(neighbor, board, visited)
		}
	}
}

func findNeighbors(currentIndex [2]int, board [][]byte) [][2]int {
	neighbors := [][2]int{}

	if currentIndex[0] < len(board)-1 {
		neighbors = append(neighbors, [2]int{currentIndex[0] + 1, currentIndex[1]})
	}
	if currentIndex[1] < len(board[0])-1 {
		neighbors = append(neighbors, [2]int{currentIndex[0], currentIndex[1] + 1})
	}
	if currentIndex[0] > 0 {
		neighbors = append(neighbors, [2]int{currentIndex[0] - 1, currentIndex[1]})
	}
	if currentIndex[1] > 0 {
		neighbors = append(neighbors, [2]int{currentIndex[0], currentIndex[1] - 1})
	}
	return neighbors
}