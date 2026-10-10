package minimumfallingpathsum

func minFallingPathSum(matrix [][]int) int {
	min_sum := 1000000000000
	cache := map[[2]int]int{}
	for j := 0; j < len(matrix[0]); j++ {
		current_sum := recursiveHelper(
			matrix,
			0,
			j,
			cache,
		)

		if current_sum < min_sum {
			min_sum = current_sum
		}
	}
	return min_sum
}

func recursiveHelper(matrix [][]int, i int, j int, cache map[[2]int]int) int {
	if j < 0 || j == len(matrix[0]) {
		return 1000000000000
	} else if i == len(matrix) {
		return 0
	}

	if value, exists := cache[[2]int{i, j}]; exists {
		return value
	}

	moves := [][2]int{
		{1, 0},
		{1, 1},
		{1, -1},
	}

	min_sum := 1000000000000

	for move := 0; move < len(moves); move++ {
		current_sum := matrix[i][j] + recursiveHelper(
			matrix,
			i+moves[move][0],
			j+moves[move][1],
			cache,
		)
		if current_sum < min_sum {
			min_sum = current_sum
		}
	}

	cache[[2]int{i, j}] = min_sum
	return cache[[2]int{i, j}]
}
