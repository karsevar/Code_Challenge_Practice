// Editorial solution where you use a recursion function in order to traverse through the matrix and use
// the input grid matrix to mark whether a cell has been visited or not.
// time complexity O(n*m) and space complexity O(n*m)
func numIslands(grid [][]byte) int {
	islandCount := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' {
				islandCount += 1
				recursionHelper(i, j, grid)
			}
		}
	}

	return islandCount
}

func recursionHelper(i int, j int, grid [][]byte) {
	if i < 0 || j < 0 || i >= len(grid) || j >= len(grid[0]) {
		return
	}

	if grid[i][j] == '0' {
		return
	}

	grid[i][j] = '0'

	recursionHelper(i-1, j, grid)
	recursionHelper(i+1, j, grid)
	recursionHelper(i, j-1, grid)
	recursionHelper(i, j+1, grid)
}