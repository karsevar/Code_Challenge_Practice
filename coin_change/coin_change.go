package coinchange

func coinChange(coins []int, amount int) int {
	cache := map[int]int{}
	minCount := recursionHelper(
		coins,
		amount,
		cache,
	)

	if minCount >= 1000000000 {
		minCount = -1
	}

	return minCount
}

func recursionHelper(coins []int, amount int, cache map[int]int) int {
	if amount == 0 {
		return 0
	}

	if amount < 0 {
		return 1000000000
	}

	if value, exists := cache[amount]; exists {
		return value
	}

	minCount := 1000000000

	for i := 0; i < len(coins); i++ {
		remainingCoins := recursionHelper(
			coins,
			amount-coins[i],
			cache,
		)

		currentCount := 1 + remainingCoins

		if currentCount < minCount {
			minCount = currentCount
		}
	}

	cache[amount] = minCount

	return minCount
}
