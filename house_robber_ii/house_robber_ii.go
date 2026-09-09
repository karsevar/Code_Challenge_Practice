package houserobberii

func rob(nums []int) int {
	if len(nums) <= 1 {
		return nums[0]
	}

	excludeFirst := recursionHelper(
		nums[1:],
		0,
		map[int]int{},
	)
	excludeLast := recursionHelper(
		nums[:len(nums)-1],
		0,
		map[int]int{},
	)
	if excludeFirst > excludeLast {
		return excludeFirst
	}
	return excludeLast
}

func recursionHelper(nums []int, index int, cache map[int]int) int {
	if index >= len(nums) {
		return 0
	}

	if value, exists := cache[index]; exists {
		return value
	}

	skip := recursionHelper(
		nums,
		index+1,
		cache,
	)

	take := nums[index] + recursionHelper(
		nums,
		index+2,
		cache,
	)

	if skip > take {
		cache[index] = skip
	} else {
		cache[index] = take
	}

	return cache[index]
}
