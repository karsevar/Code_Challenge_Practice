package availablecapturesforrook

import "fmt"

func numRookCaptures(board [][]byte) int {
	rookLocation := findRook(board)

	rookMoves := [][]int{
		// up
		{-1, 0},
		// down
		{1, 0},
		// left
		{0, -1},
		// right
		{0, 1},
	}

	count := 0

	for _, move := range rookMoves {
		fmt.Println("move: ", move)
		count += rookMoveHelper(
			rookLocation[0]+move[0],
			rookLocation[1]+move[1],
			move,
			board,
		)
	}
	return count
}

func findRook(board [][]byte) []int {
	rookLocation := []int{}
	for j := 0; j < len(board); j++ {
		for i := 0; i < len(board[0]); i++ {
			if string(board[j][i]) == "R" {
				rookLocation = append(rookLocation, j)
				rookLocation = append(rookLocation, i)
			}
		}
	}

	return rookLocation
}

func rookMoveHelper(j int, i int, move []int, board [][]byte) int {
	count := 0
	for j < len(board) && j >= 0 && i < len(board[0]) && i >= 0 {
		if string(board[j][i]) == "p" {
			count += 1
			break
		}

		if string(board[j][i]) != "p" && string(board[j][i]) != "." {
			break
		}

		j += move[0]
		i += move[1]
	}

	return count
}
