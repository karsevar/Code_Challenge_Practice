package restoreipaddresses

import (
	"strconv"
	"strings"
)

func restoreIpAddresses(s string) []string {
	// first I will need to create a results array that will carry all the conbinations of valid ip addresses

	// create a recursive function that will take a state argument, s, and results

	// return results

	var results []string
	var state []string
	recursion_helper(state, s, &results)
	return results
}

func recursion_helper(state []string, s string, results *[]string) {

	if len(state) == 4 && len(s) == 0 {
		state_str := strings.Join(state[:], ".")
		*results = append(*results, state_str)
		return
	} else if len(state) < 4 && len(s) > 0 {
		for i := 1; i < 4; i++ {
			if i > len(s) {
				break
			}

			if checkIpDigit(s[0:i]) {
				state = append(state, s[0:i])
				recursion_helper(state, s[i:], results)
				state = state[:len(state)-1]
			}
		}
	}
}

func checkIpDigit(digit string) bool {
	if string(digit[0]) == "0" && len(digit) > 1 {
		return false
	}

	if i, _ := strconv.Atoi(digit); i <= 255 {
		return true
	}

	return false
}
