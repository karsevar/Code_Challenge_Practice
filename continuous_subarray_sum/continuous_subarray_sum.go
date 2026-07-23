package continuoussubarraysum

func checkSubarraySum(nums []int, k int) bool {
	freq := map[int]int{0: -1}
	totalSum := 0

	for i := 0; i < len(nums); i++ {
		totalSum += nums[i]
		remainder := totalSum % k
		if startIndex, exists := freq[remainder]; exists {
			if i-startIndex > 1 {
				return true
			}
		} else {
			freq[remainder] = i
		}
	}
	return false
}
