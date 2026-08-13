package generateparentheses

import (
	"strings"
)

func generateParenthesis(n int) []string {
	results := []string{}

	recursiveHelper(
		[]string{},
		n,
		n,
		&results,
	)

	return results
}

func recursiveHelper(state []string, closingCounter int, openingCounter int, results *[]string) {
	if closingCounter == 0 && openingCounter == 0 {
		*results = append(*results, strings.Join(state, ""))
		return
	}

	if closingCounter < 0 || openingCounter < 0 {
		return
	}

	if closingCounter > 0 || openingCounter > 0 {
		for _, choice := range []string{"(", ")"} {
			if len(state) == 0 && choice == ")" {
				continue
			}

			if openingCounter == 0 && choice == "(" {
				continue
			}

			if openingCounter == closingCounter && choice == ")" {
				continue
			}

			if choice == "(" {
				openingCounter -= 1
			} else {
				closingCounter -= 1
			}

			state = append(state, choice)
			recursiveHelper(
				state,
				closingCounter,
				openingCounter,
				results,
			)
			state = state[:len(state)-1]

			if choice == "(" {
				openingCounter += 1
			} else {
				closingCounter += 1
			}
		}
	}
}
