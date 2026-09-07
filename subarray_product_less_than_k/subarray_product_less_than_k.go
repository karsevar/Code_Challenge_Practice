package subarrayproductlessthank

func numSubarrayProductLessThanK(nums []int, k int) int {
	leftPointer := 0
	currentProduct := 1
	subarrayCount := 0

	for rightPointer := 0; rightPointer < len(nums); rightPointer++ {
		currentProduct *= nums[rightPointer]

		for leftPointer <= rightPointer && currentProduct >= k {
			currentProduct /= nums[leftPointer]
			leftPointer += 1
		}

		if currentProduct < k {
			subarrayCount += rightPointer - leftPointer + 1
		}
	}

	return subarrayCount
}
