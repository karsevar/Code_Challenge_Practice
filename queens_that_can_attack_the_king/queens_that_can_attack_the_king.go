package queensthatcanattacktheking

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	queenMap := map[[2]int]bool{}

	for i := 0; i < len(queens); i++ {
		dataPoint := [2]int{queens[i][0], queens[i][1]}
		queenMap[dataPoint] = true
	}

	results := [][]int{}

	moves := [][]int{
		{-1, 0},
		{-1, -1},
		{-1, 1},
		{0, 1},
		{0, -1},
		{1, 0},
		{1, -1},
		{1, 1},
	}

	for i := 0; i < len(moves); i++ {
		recursionHelper(
			king[0],
			king[1],
			queenMap,
			&results,
			moves[i],
		)
	}

	return results
}

func recursionHelper(kingJ int, kingI int, queens map[[2]int]bool, results *[][]int, move []int) {
	if kingJ >= 8 || kingI >= 8 || kingJ < 0 || kingI < 0 {
		return
	}

	dataPoint := [2]int{kingJ, kingI}
	if _, exists := queens[dataPoint]; exists {
		*results = append(*results, []int{kingJ, kingI})
		return
	}

	recursionHelper(
		kingJ+move[0],
		kingI+move[1],
		queens,
		results,
		move,
	)
}
