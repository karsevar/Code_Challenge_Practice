package targetsum

func findTargetSumWays(nums []int, target int) int {
	results := recursionHelper(0, 0, target, nums)
	return results
}

func recursionHelper(
	currentSum int,
	index int,
	target int,
	nums []int,
) int {
	if index == len(nums) {
		if target == currentSum {
			return 1
		}
		return 0
	}

	negativeResults := recursionHelper(
		currentSum-nums[index],
		index+1,
		target,
		nums,
	)

	positiveResults := recursionHelper(
		currentSum+nums[index],
		index+1,
		target,
		nums,
	)

	return negativeResults + positiveResults
}
