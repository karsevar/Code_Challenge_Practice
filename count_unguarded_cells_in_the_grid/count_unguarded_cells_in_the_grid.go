package countunguardedcellsinthegrid

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	matrix := make([][]int, m)
	for i := 0; i < m; i++ {
		matrix[i] = make([]int, n)
	}

	for i := 0; i < len(guards); i++ {
		matrix[guards[i][0]][guards[i][1]] = 1
	}

	for i := 0; i < len(walls); i++ {
		matrix[walls[i][0]][walls[i][1]] = 2
	}

	moves := [][]int{
		{1, 0},
		{-1, 0},
		{0, 1},
		{0, -1},
	}

	for _, guard := range guards {
		for _, move := range moves {
			recursionHelper(
				guard[0]+move[0],
				guard[1]+move[1],
				matrix,
				move,
			)
		}
	}

	count := 0

	for j := 0; j < len(matrix); j++ {
		for i := 0; i < len(matrix[0]); i++ {
			if matrix[j][i] == 0 {
				count += 1
			}
		}
	}

	return count
}

func recursionHelper(j int, i int, matrix [][]int, move []int) {
	if j >= len(matrix) || i >= len(matrix[0]) || i < 0 || j < 0 {
		return
	}
	if matrix[j][i] == 1 || matrix[j][i] == 2 {
		return
	}

	matrix[j][i] = 3
	recursionHelper(
		j+move[0],
		i+move[1],
		matrix,
		move,
	)
}
