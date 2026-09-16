package knightprobabilityinchessboard

import "math"

func knightProbability(n int, k int, row int, column int) float64 {
	probability := math.Pow(float64(8), float64(k))
	return float64(recursionHelper(
		column,
		row,
		k,
		n,
		map[[3]int]float64{},
	)) / probability
}

func recursionHelper(j int, i int, k int, n int, cache map[[3]int]float64) float64 {
	if j >= n || j < 0 || i >= n || i < 0 {
		return 0
	}
	if j < n && i < n && i >= 0 && j >= 0 && k == 0 {
		return 1
	}

	dataPoint := [3]int{j, i, k}
	if value, exists := cache[dataPoint]; exists {
		return value
	}

	moves := [][]int{
		// up left and right
		{-2, -1},
		{-2, 1},

		// down left and right
		{2, -1},
		{2, 1},

		// left down and up
		{-1, -2},
		{1, -2},

		// right down and up
		{-1, 2},
		{1, 2},
	}

	moveCount := 0.0

	for _, move := range moves {
		moveCount += recursionHelper(
			j+move[0],
			i+move[1],
			k-1,
			n,
			cache,
		)
	}

	cache[dataPoint] = moveCount
	return cache[dataPoint]
}
