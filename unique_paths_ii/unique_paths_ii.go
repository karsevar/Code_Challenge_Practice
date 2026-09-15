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
