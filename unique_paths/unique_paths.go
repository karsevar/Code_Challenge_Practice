package uniquepaths

func uniquePaths(m int, n int) int {
	return recursionHelper(
		1,
		1,
		m,
		n,
		map[[2]int]int{},
	)
}

func recursionHelper(mIndex int, nIndex int, m int, n int, cache map[[2]int]int) int {
	if mIndex > m && nIndex < n {
		return 0
	} else if nIndex > n && mIndex < m {
		return 0
	} else if mIndex == m && nIndex == n {
		return 1
	}

	indexPoint := [2]int{mIndex, nIndex}

	if value, exists := cache[indexPoint]; exists {
		return value
	}

	cache[indexPoint] = recursionHelper(mIndex+1, nIndex, m, n, cache) + recursionHelper(mIndex, nIndex+1, m, n, cache)
	return cache[indexPoint]
}

func uniquePathsTabulation(m int, n int) int {
	dp := make([][]int, m)

	for i := range dp {
		dp[i] = make([]int, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if j == 0 {
				dp[i][j] = 1
			} else if i == 0 {
				dp[i][j] = 1
			} else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}
		}
	}

	return dp[m-1][n-1]
}
