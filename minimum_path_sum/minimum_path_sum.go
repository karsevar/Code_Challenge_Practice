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
