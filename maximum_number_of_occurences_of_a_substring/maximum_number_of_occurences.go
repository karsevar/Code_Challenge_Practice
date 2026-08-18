package maximumnumberofoccurencesofasubstring

func maxFreq(s string, maxLetters int, minSize int, maxSize int) int {
	leftPointer := 0
	subSequences := map[string]int{}
	uniqueLetters := map[byte]int{}
	maxCount := 0

	for rightPointer := 0; rightPointer < len(s); rightPointer++ {
		count, exists := uniqueLetters[s[rightPointer]]

		if exists {
			uniqueLetters[s[rightPointer]] = count + 1
		} else {
			uniqueLetters[s[rightPointer]] = 1
		}

		for len(uniqueLetters) > maxLetters || minSize < rightPointer-leftPointer+1 {
			count, exists := uniqueLetters[s[leftPointer]]
			if exists {
				if count > 1 {
					uniqueLetters[s[leftPointer]] = count - 1
				} else {
					delete(uniqueLetters, s[leftPointer])
				}
			}
			leftPointer += 1
		}

		curr := string(s[leftPointer : rightPointer+1])

		if minSize == len(curr) {
			count, exists := subSequences[curr]
			if exists {
				count = count + 1
				subSequences[curr] = count
			} else {
				count = 1
				subSequences[curr] = count
			}

			if count > maxCount {
				maxCount = count
			}
		}
	}

	return maxCount
}
