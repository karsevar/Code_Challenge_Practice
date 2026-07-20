package minimumsizesubarraysum

func minSubArrayLen(target int, nums []int) int {
	// so for this problem I will need to keep a running some of all the values that are processed by the right pointer and when that sum becomes greater than or equal to the target I have to shrink the running sum by incrementing the left pointer

	// create a minimum length variable start at 0
	// create a running sum value variable
	// create a right pointer that will start at index 0

	// create a for loop that will have the right pointer as the index variable
	// add nums[right_pointer] to the running sum
	// if running sum is equal to or greater than target update minimum_length if it is less in length.
	// create while loop that will increment left_pointer until sum is less than target

	minimumLength := 0
	sumTotal := 0
	leftPointer := 0
	currentLength := 0

	for i := 0; i < len(nums); i++ {
		sumTotal += nums[i]
		currentLength += 1
		if sumTotal >= target {
			if minimumLength > currentLength || minimumLength == 0 {
				minimumLength = currentLength
			}
		}

		for sumTotal >= target {

			if minimumLength > currentLength || minimumLength == 0 {
				minimumLength = currentLength
			}

			sumTotal -= nums[leftPointer]
			currentLength -= 1
			leftPointer += 1
		}
	}
	return minimumLength
}
