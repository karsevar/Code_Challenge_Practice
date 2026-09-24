package laststoneweight

import (
	"sort"
)

func lastStoneWeight(stones []int) int {
	for len(stones) > 1 {
		sort.Slice(stones, func(i, j int) bool {
			return stones[i] > stones[j]
		})

		if stones[0] != stones[1] {
			newStone := stones[0] - stones[1]
			stones[1] = newStone
			stones = stones[1:]
		} else if stones[0] == stones[1] {
			stones = stones[2:]
		}
	}

	result := 0

	if len(stones) == 1 {
		result = stones[0]
	}

	return result
}
