package coinchangeii

func change(amount int, coins []int) int {
	return recursionHelper(
		0,
		amount,
		coins,
		map[[2]int]int{},
	)
}

func recursionHelper(
	index int,
	amount int,
	coins []int,
	cache map[[2]int]int,
) int {
	if amount == 0 {
		return 1
	}

	if amount < 0 {
		return 0
	}

	if index >= len(coins) {
		return 0
	}

	dataPoint := [2]int{amount, index}

	if value, exists := cache[dataPoint]; exists {
		return value
	}

	take := recursionHelper(
		index,
		amount-coins[index],
		coins,
		cache,
	)

	skip := recursionHelper(
		index+1,
		amount,
		coins,
		cache,
	)

	cache[dataPoint] = take + skip

	return cache[dataPoint]
}
