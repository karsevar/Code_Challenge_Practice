package combinationsumiii

func combinationSum3(k int, n int) [][]int {
	results := [][]int{}

	recursionHelper(
		[]int{},
		1,
		n,
		k,
		&results,
	)

	return results
}

func recursionHelper(state []int, index int, target int, k int, results *[][]int) {
	if len(state) == k && target == 0 {
		duplicateState := append([]int(nil), state...)
		*results = append(*results, duplicateState)
		return
	}

	if target > 0 {
		for num := index; num < 10; num++ {
			state = append(state, num)
			recursionHelper(
				state,
				num+1,
				target-num,
				k,
				results,
			)
			state = state[:len(state)-1]
		}
	}
}
