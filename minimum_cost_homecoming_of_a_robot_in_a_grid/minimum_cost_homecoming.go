package minimumcosthomecomingofarobotinagrid

// editorial solution.
// interestingly the explaination for this solution is that we don't need to explore the grid to see if
// we can find a minimum cost path and that the shortest amount of moves the robot can make will always be
// the optimal path with the least cost in the grid.
// time complexity: O(row difference + column difference)
func minCost(startPos []int, homePos []int, rowCosts []int, colCosts []int) int {
	cost := 0

	if startPos[0] < homePos[0] {
		for row := startPos[0] + 1; row < homePos[0]+1; row++ {
			cost += rowCosts[row]
		}
	} else {
		for row := startPos[0] - 1; row > homePos[0]-1; row-- {
			cost += rowCosts[row]
		}
	}

	if startPos[1] < homePos[1] {
		for col := startPos[1] + 1; col < homePos[1]+1; col++ {
			cost += colCosts[col]
		}
	} else {
		for col := startPos[1] - 1; col > homePos[1]-1; col-- {
			cost += colCosts[col]
		}
	}

	return cost
}
