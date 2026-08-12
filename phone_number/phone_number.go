package phonenumber

import (
	"strings"
)

func letterCombinations(digits string) []string {
	letterMap := map[string][]string{
		"2": []string{
			"a", "b", "c",
		},
		"3": []string{
			"d", "e", "f",
		},
		"4": []string{
			"g", "h", "i",
		},
		"5": []string{
			"j", "k", "l",
		},
		"6": []string{
			"m", "n", "o",
		},
		"7": []string{
			"p", "q", "r", "s",
		},
		"8": []string{
			"t", "u", "v",
		},
		"9": []string{
			"w", "y", "x", "z",
		},
	}

	results := []string{}

	recursion_helper(
		[]string{},
		digits,
		0,
		&results,
		letterMap,
	)

	return results
}

func recursion_helper(state []string, digits string, index int, results *[]string, letterCombinations map[string][]string) {
	if index == len(digits) {
		combination := strings.Join(state, "")
		*results = append(*results, combination)
		return
	}

	if index < len(digits) {
		letters, exists := letterCombinations[string(digits[index])]
		if exists {
			for _, letter := range letters {
				state = append(state, letter)
				recursion_helper(
					state,
					digits,
					index+1,
					results,
					letterCombinations,
				)
				state = state[:len(state)-1]
			}
		}
	}
}
