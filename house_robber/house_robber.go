package houserobber

func rob(nums []int) int {
	cache := map[int]int{
		len(nums):     0,
		len(nums) + 1: 0,
		len(nums) + 2: 0,
	}
	return recursionHelper(
		0,
		nums,
		cache,
	)
}

func recursionHelper(index int, nums []int, cache map[int]int) int {
	if value, existing := cache[index]; existing {
		return value
	}

	skip := recursionHelper(
		index+1,
		nums,
		cache,
	)

	take := nums[index] + recursionHelper(
		index+2,
		nums,
		cache,
	)

	var maxValue int
	if skip > take {
		maxValue = skip
	} else {
		maxValue = take
	}

	cache[index] = maxValue
	return cache[index]
}
