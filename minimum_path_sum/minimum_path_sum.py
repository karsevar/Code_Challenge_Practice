class Solution:
    # Included a cache to the bruteforce solution which will most likely decrease the time complexity 
    # to O(n*m) where n is the j axis and m is the i axis. 
    # space complexity will be most likely the same as well (O(n*m))
    def minPathSum(self, grid: List[List[int]]) -> int:
        # okay for this problem all we need to do is use the same iIndex and jIndex methodology but we need to find the value that creates the smallest sum. 
        # two possible moves in the grid right or down. This kind possibly be the same as the unique paths problem

        cache = {}

        return self.recursion_helper(
            grid,
            0,
            0,
            cache
        )

    def recursion_helper(self, grid: List[List[int]], j: int, i: int, cache: dict[int, int]) -> int:
        if j >= len(grid) and i < len(grid[0]):
            return 1000000
        elif i >= len(grid[0]) and j < len(grid):
            return 1000000
        elif j == len(grid)-1 and i == len(grid[0])-1:
            return grid[j][i]

        if (j, i) in cache:
            return cache[(j, i)]

        cache[(j, i)] = grid[j][i] + min(
            self.recursion_helper(
                grid,
                j+1,
                i,
                cache
            ),
            self.recursion_helper(
                grid,
                j,
                i+1,
                cache
            )
        )

        return cache[(j, i)]