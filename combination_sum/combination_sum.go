import (
	"fmt"
)

func combinationSum(candidates []int, target int) [][]int {
	results := [][]int{}
	recursionHelper([]int{}, 0, candidates, target, &results)
	return results
}

func recursionHelper(state []int, index int, candidates []int, target int, results *[][]int) {
	if target == 0 {
		combination := append([]int{}, state...)
		*results = append(*results, combination)
		return
	}

	if target > 0 {
		for i := index; i < len(candidates); i++ {
			state = append(state, candidates[i])
			recursionHelper(state, i, candidates, target-candidates[i], results)
			state = state[:len(state)-1]
		}
	}
}