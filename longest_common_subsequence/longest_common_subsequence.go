package longestcommonsubsequence

func longestCommonSubsequence(text1 string, text2 string) int {
	cache := map[[2]int]int{}

	return recursionHelper(
		0,
		0,
		text1,
		text2,
		cache,
	)
}

func recursionHelper(i int, j int, text1 string, text2 string, cache map[[2]int]int) int {
	if i >= len(text1) || j >= len(text2) {
		return 0
	}

	dataPoint := [2]int{i, j}

	if value, exists := cache[dataPoint]; exists {
		return value
	}

	if text1[i] == text2[j] {
		return 1 + recursionHelper(
			i+1,
			j+1,
			text1,
			text2,
			cache,
		)
	}

	moveI := recursionHelper(
		i+1,
		j,
		text1,
		text2,
		cache,
	)

	moveJ := recursionHelper(
		i,
		j+1,
		text1,
		text2,
		cache,
	)

	var maxMoveValue int
	if moveI > moveJ {
		maxMoveValue = moveI
	} else {
		maxMoveValue = moveJ
	}

	cache[dataPoint] = maxMoveValue

	return cache[dataPoint]
}
