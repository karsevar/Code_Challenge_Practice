package maximumproductsubarray

// Bruteforce solution written in golang. Does not pass the 183 test case in the same way as the python solution.

func maxProduct(nums []int) int {
	return recursionHelper(
		0,
		nums,
	)
}

func recursionHelper(index int, nums []int) int {
	maxProduct := -1000000000
	currentProduct := 1
	for i := index; i < len(nums); i++ {
		currentProduct *= nums[i]

		if maxProduct < currentProduct {
			maxProduct = currentProduct
		}

		recursionProduct := recursionHelper(
			i+1,
			nums,
		)

		if recursionProduct > maxProduct {
			maxProduct = recursionProduct
		}
	}

	return maxProduct
}
