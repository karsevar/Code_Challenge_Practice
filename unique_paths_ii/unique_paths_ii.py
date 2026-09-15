class Solution:
    # Brutefore solution which most likely has a time complexity of O(2n*m) since the matrix is of n rows and m columns and there are a total of two choices to decide on. 
    # Easiest way to decrease the time complexity is add a cache. Which might change the time complexity equation to O(n*m).
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # This problem looks pretty straightforward.
        # We can most likely solve this problem through perhaps including whether the current index in the matrix falls under 1. If the current index position falls under 1 when all we need to do is return 0 for that specific path.

        # bruteforce method: create a recursion function that will take i index, j index and obstacleGrid as arguments.

        cache = {} # structure of cache {(j, i): count}

        return self.recursion_helper(
            0,
            0,
            obstacleGrid,
            cache,
        )


    def recursion_helper(self, i: int, j: int, obstacleGrid: list[list[int]], cache: dict[tuple[int], int]) -> int:
        # base case:
        # if the final index is equal to len(obstacleGrid) and len(obstacleGrid[0]) return 1
        # if the j index falls outside of len(obstacleGrid) or i index falls outside of len(obstacleGrid[0]) then return 0
        # if current index falls into a cell that contains 1 then return 0

        # recursive case:
        # create a variable that will contain all recursive calls that moves the robot to the right
        # create a variable that will contain all recursive calls that moves the robot down
        # return right and down recursive calls

        if j >= len(obstacleGrid) or i >= len(obstacleGrid[0]):
            return 0
        if obstacleGrid[j][i] == 1:
            return 0
        if j == len(obstacleGrid) - 1 and i == len(obstacleGrid[0]) - 1:
            return 1

        if (j, i) in cache:
            return cache[(j, i)]

        rightMove = self.recursion_helper(
            i + 1,
            j,
            obstacleGrid,
            cache,
        )
        downMove = self.recursion_helper(
            i,
            j + 1,
            obstacleGrid,
            cache,
        )

        cache[(j, i)] = rightMove + downMove
        return cache[(j, i)]