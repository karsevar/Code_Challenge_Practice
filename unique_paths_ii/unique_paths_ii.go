package uniquepathsii

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	cache := map[[2]int]int{}
	return recursionHelper(
		0,
		0,
		obstacleGrid,
		cache,
	)
}

func recursionHelper(i int, j int, obstacleGrid [][]int, cache map[[2]int]int) int {
	if j >= len(obstacleGrid) || i >= len(obstacleGrid[0]) {
		return 0
	}

	if obstacleGrid[j][i] == 1 {
		return 0
	}

	if j == len(obstacleGrid)-1 && i == len(obstacleGrid[0])-1 {
		return 1
	}

	dataPoint := [2]int{j, i}

	if value, exists := cache[dataPoint]; exists {
		return value
	}

	cache[dataPoint] = recursionHelper(i+1, j, obstacleGrid, cache) + recursionHelper(i, j+1, obstacleGrid, cache)
	return cache[dataPoint]
}

func uniquePathsWithObstaclesTabulation(obstacleGrid [][]int) int {
	n := len(obstacleGrid)
	m := len(obstacleGrid[0])

	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, m)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if obstacleGrid[i][j] == 1 {
				dp[i][j] = 0
			} else if i == 0 && j == 0 {
				dp[i][j] = 1
			} else if i == 0 {
				dp[i][j] = dp[i][j-1]
			} else if j == 0 {
				dp[i][j] = dp[i-1][j]
			} else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}
		}
	}

	return dp[n-1][m-1]
}
