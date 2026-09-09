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
