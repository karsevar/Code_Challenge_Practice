package mincostclimbingstairs

func minCostClimbingStairs(cost []int) int {
	cache := map[int]int{
		len(cost):     0,
		len(cost) + 1: 0,
		len(cost) + 2: 0,
	}

	var minCost int

	oneStep := recursionHelper(
		cost,
		0,
		cache,
	)
	twoStep := recursionHelper(
		cost,
		1,
		cache,
	)

	if oneStep > twoStep {
		minCost = twoStep
	} else {
		minCost = oneStep
	}

	return minCost
}

func recursionHelper(cost []int, index int, cache map[int]int) int {
	if value, exists := cache[index]; exists {
		return value
	}

	oneStep := recursionHelper(cost, index+1, cache)
	twoStep := recursionHelper(cost, index+2, cache)

	var minCost int

	if oneStep < twoStep {
		minCost = oneStep
	} else {
		minCost = twoStep
	}

	cache[index] = cost[index] + minCost
	return cache[index]
}
