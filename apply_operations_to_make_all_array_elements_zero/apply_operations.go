package applyoperationstomakeallarrayelementszero

// Editorial solution that uses the same greedly approach as the one for python.
// Currently this only passes 1027 of the 1029 test cases. Most likely the only way is to
// use the sliding window approach. Will revisit this problem later.
func checkArray(nums []int, k int) bool {
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			continue
		}

		if i+k > len(nums) {
			return false
		}

		amount := nums[i]
		for j := i; j < i+k; j++ {
			nums[j] -= amount

			if nums[j] < 0 {
				return false
			}
		}
	}

	return true
}
