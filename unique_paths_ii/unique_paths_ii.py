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


class SolutionTabulation:
    # okay so through tabulation we can think of this problem in much the same way as unique paths 1. In that we are looking for all the unique paths the robot can take to reach grid[m-1][n-1]. The only difference is the need to label the obstruction space as 0 since we want to discount it within the tally of possible paths the robot can take.

    # time complexity can be conceptualized as O(n*m) where we are only looping through the rows and columns of the input obstacleGrid variable
    # space complexity can be conceptualized as O(n*m) as well since we are creating a dp array that mirrors the dimensions of the input obstacleGrid array.
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # create a dp array that is of len(obstacleGrid) rows and len(obstableGrid[0]) columns. 

        # create a nested for loop
        # loop through rows of obstacleGrid
        # loop through the columns of obstableGrid
        # if obstableGrid[i][j] == 1 then mark the space as zero.
        # if len(obstacleGrid)-1 == i then mark the space as 1
        # if len(obstableGrid[0])-1 == j then mark the space as 1
        # else mark the space as dp[i-1][j] + dp[i][j-1]

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]