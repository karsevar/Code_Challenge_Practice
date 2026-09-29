package wordbreak

func wordBreak(s string, wordDict []string) bool {
	dp := make([]bool, len(s)+1)

	dp[0] = true

	wordMap := make(map[string]bool)

	for word := 0; word < len(wordDict); word++ {
		wordMap[wordDict[word]] = true
	}

	for i := 1; i < len(s)+1; i++ {
		for j := 0; j < i; j++ {
			if dp[j] == false {
				continue
			}

			substring := string(s[j:i])

			if _, exists := wordMap[substring]; exists {
				dp[i] = true
				break
			}
		}
	}

	return dp[len(s)]
}
