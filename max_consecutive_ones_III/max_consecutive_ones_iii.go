package maxconsecutiveonesiii

func longestOnes(nums []int, k int) int {
	// create a convert zero counter initialize to zero
	// create maximum length variable initialize to zero
	// create left pointer value initialize to zero
	// create current length variable

	// create a for loop that will be used as right pointer
	// if nums[right_pointer] is 1 increment current length variable
	// if nums[right_pointer] is 0 check if convert zero counter is not more than k
	// if true increment current length variable and increment convert zero counter
	// if false create while loop that terminates when increment convert zero counter is not greater than k

	zeroCounter := 0
	maximumLength := 0
	leftPointer := 0
	currentLength := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			currentLength += 1
		} else {
			if zeroCounter <= k {
				zeroCounter += 1
				currentLength += 1
			}
			for zeroCounter > k {
				if nums[leftPointer] == 1 {
					currentLength -= 1
				} else {
					currentLength -= 1
					zeroCounter -= 1
				}
				leftPointer += 1
			}
		}

		if currentLength > maximumLength {
			maximumLength = currentLength
		}
	}
	return maximumLength
}
