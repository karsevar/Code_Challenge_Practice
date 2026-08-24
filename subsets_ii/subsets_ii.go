package subsetsii

import (
	"sort"
)

func subsetsWithDup(nums []int) [][]int {
	results := [][]int{}

	sort.Ints(nums)

	subsetsRecursion(
		[]int{},
		0,
		nums,
		&results,
	)

	return results
}

func subsetsRecursion(state []int, index int, nums []int, results *[][]int) {
	duplicateState := append([]int(nil), state...)
	*results = append(*results, duplicateState)

	for i := index; i < len(nums); i++ {
		if i > index && nums[i] == nums[i-1] {
			continue
		}
		state = append(state, nums[i])
		subsetsRecursion(
			state,
			i+1,
			nums,
			results,
		)
		state = state[:len(state)-1]
	}
}
