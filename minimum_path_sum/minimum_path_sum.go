package minimumpathsum

func minPathSum(grid [][]int) int {
	cache := map[[2]int]int{}
	return recursionHelper(
		0,
		0,
		grid,
		cache,
	)
}

func recursionHelper(j int, i int, grid [][]int, cache map[[2]int]int) int {
	if j >= len(grid) || i >= len(grid[0]) {
		return 10000000
	} else if j == len(grid)-1 && i == len(grid[0])-1 {
		return grid[j][i]
	}

	dataPoint := [2]int{j, i}

	if value, exists := cache[dataPoint]; exists {
		return value
	}

	currentSum := grid[j][i]

	rightMovement := recursionHelper(j, i+1, grid, cache)
	downMovement := recursionHelper(j+1, i, grid, cache)

	if rightMovement < downMovement {
		currentSum += rightMovement
	} else {
		currentSum += downMovement
	}

	cache[dataPoint] = currentSum

	return cache[dataPoint]
}

func minPathSumTabulation(grid [][]int) int {
	dp := make([][]int, len(grid))

	for i := range dp {
		dp[i] = make([]int, len(grid[0]))
	}

	dp[0][0] = grid[0][0]

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if i-1 < 0 && j-1 < 0 {
				continue
			} else if i-1 < 0 {
				dp[i][j] = grid[i][j] + dp[i][j-1]
			} else if j-1 < 0 {
				dp[i][j] = grid[i][j] + dp[i-1][j]
			} else {
				if dp[i-1][j] > dp[i][j-1] {
					dp[i][j] = grid[i][j] + dp[i][j-1]
				} else {
					dp[i][j] = grid[i][j] + dp[i-1][j]
				}
			}
		}
	}

	return dp[len(grid)-1][len(grid[0])-1]
}
