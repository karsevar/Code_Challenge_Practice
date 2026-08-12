package combinationsumii

import "slices"

func combinationSum2(candidates []int, target int) [][]int {
	results := [][]int{}
	slices.Sort(candidates)

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
			if i > index && candidates[i] == candidates[i-1] {
				continue
			}
			state = append(state, candidates[i])
			recursionHelper(state, i+1, candidates, target-candidates[i], results)
			state = state[:len(state)-1]
		}
	}
}
