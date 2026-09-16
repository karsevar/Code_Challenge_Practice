package executionofallsuffixinstructionsstayingingrid

func executeInstructions(n int, startPos []int, s string) []int {
	results := []int{}
	for sIndex := 0; sIndex < len(s); sIndex++ {
		count := recursionHelper(
			startPos[0],
			startPos[1],
			sIndex,
			s,
			n,
		)
		results = append(results, count)
	}
	return results
}

func recursionHelper(j int, i int, sIndex int, s string, n int) int {
	if j >= n || j < 0 || i >= n || i < 0 {
		return -1
	}
	if sIndex == len(s) {
		return 0
	}

	moveMap := map[string]int{
		"L": -1,
		"R": 1,
		"D": 1,
		"U": -1,
	}

	currentCount := 1

	if value, exists := moveMap[string(s[sIndex])]; exists {
		if string(s[sIndex]) == "L" || string(s[sIndex]) == "R" {
			currentCount += recursionHelper(
				j,
				i+value,
				sIndex+1,
				s,
				n,
			)
		} else if string(s[sIndex]) == "D" || string(s[sIndex]) == "U" {
			currentCount += recursionHelper(
				j+value,
				i,
				sIndex+1,
				s,
				n,
			)
		}
	}

	return currentCount
}
