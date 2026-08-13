package repeateddnasequence

func findRepeatedDnaSequences(s string) []string {
	results := []string{}
	hashMap := map[string]int{}

	if len(s) >= 10 {
		for i := 0; i < len(s)-10+1; i++ {
			currentSequence := string(s[i : i+10])
			if value, exists := hashMap[currentSequence]; exists {
				hashMap[currentSequence] = value + 1
			} else {
				hashMap[currentSequence] = 1
			}
		}

		for sequence, count := range hashMap {
			if count > 1 {
				results = append(results, sequence)
			}
		}
	}
	return results
}
