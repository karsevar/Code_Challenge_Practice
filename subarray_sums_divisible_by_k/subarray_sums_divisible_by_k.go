package subarraysumsdivisiblebyk

func subarraysDivByK(nums []int, k int) int {
	// create a frequency hashmap
	// create cumulative sum variable
	// create count variable

	// create a for loop that will loop through nums
	// add current num to cumulative sum variable
	// check if cumulative sum % k is in frequency hashmap
	// if so increment count variable

	// add cumulative sum % k key to frequency hashmap

	totalSum := 0
	count := 0

	freq := map[int]int{0: 1}

	for i := 0; i < len(nums); i++ {
		totalSum += nums[i]

		remainder := totalSum % k
		if remainder < 0 {
			remainder += k
		}

		if _, exists := freq[remainder]; exists {
			count += freq[remainder]
			freq[remainder] += 1
		} else {
			freq[remainder] = 1
		}
	}
	return count

}
