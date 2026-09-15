package outofboundarypaths

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
	cache := map[[3]int]int{}
	return recursionHelper(
		startRow,
		startColumn,
		m,
		n,
		maxMove,
		cache,
	)
}

func recursionHelper(j int, i int, m int, n int, maxMove int, cache map[[3]int]int) int {
	if (j >= m || i >= n || i < 0 || j < 0) && maxMove >= 0 {
		return 1
	}
	if maxMove < 0 {
		return 0
	}

	dataPoint := [3]int{j, i, maxMove}

	if value, exists := cache[dataPoint]; exists {
		return value
	}

	rightMove := recursionHelper(
		j,
		i+1,
		m,
		n,
		maxMove-1,
		cache,
	)
	leftMove := recursionHelper(
		j,
		i-1,
		m,
		n,
		maxMove-1,
		cache,
	)
	downMove := recursionHelper(
		j+1,
		i,
		m,
		n,
		maxMove-1,
		cache,
	)
	upMove := recursionHelper(
		j-1,
		i,
		m,
		n,
		maxMove-1,
		cache,
	)

	const MOD int = 1000000007

	cache[dataPoint] = (rightMove + downMove + leftMove + upMove) % MOD
	return cache[dataPoint]
}
