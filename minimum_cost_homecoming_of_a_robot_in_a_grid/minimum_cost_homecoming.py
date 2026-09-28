class SolutionBruteforce:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        # much like the unque paths problem we have a specific place that the robot will need to go to which is homePos.
        # the bruteforce method is to simply move in the four directions until it reaches the homePos cordinates or it goes to the end of the matrix.
        # to influence the algorithm we will need to ensure that if the robot reaches the end of the matrix the returned integer needs to be very high.

        # this implementation still doesn't pass the 54th edge case due to a memory limit constraint. It seems that
        # exploring the grid is not the most optimal way to solve this problem and that speeding up the solution with a 
        # cache doesn't really fix the fact that this is not a dynamic programming problem.

        cache = {} # keys will most likely look like this {(j,i): best cost}

        return self.recursion_helper(
            startPos,
            homePos,
            rowCosts,
            colCosts,
            cache,
        )


    def recursion_helper(self, robotPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int], cache: dict[tuple[int], int]) -> int:
        if robotPos == homePos:
            return 0

        currentRow = robotPos[0]
        currentCol = robotPos[1]

        if (currentRow, currentCol) in cache:
            return cache[(currentRow, currentCol)]

        bestCost = float("inf")

        if currentRow < homePos[0]:
            newRow = currentRow + 1
            cost = rowCosts[newRow] + self.recursion_helper(
                [newRow, currentCol],
                homePos,
                rowCosts,
                colCosts,
                cache,
            )
            bestCost = min(cost, bestCost)
        elif currentRow > homePos[0]:
            newRow = currentRow - 1 
            cost = rowCosts[newRow] + self.recursion_helper(
                [newRow, currentCol],
                homePos,
                rowCosts,
                colCosts,
                cache,
            )
            bestCost = min(cost, bestCost)

        if currentCol < homePos[1]:
            newCol = currentCol + 1
            cost = colCosts[newCol] + self.recursion_helper(
                [currentRow, newCol],
                homePos,
                rowCosts,
                colCosts,
                cache,
            )
            bestCost = min(cost, bestCost)

        elif currentCol > homePos[1]:
            newCol = currentCol - 1
            cost = colCosts[newCol] + self.recursion_helper(
                [currentRow, newCol],
                homePos,
                rowCosts,
                colCosts,
                cache,
            )
            bestCost = min(cost, bestCost)

        cache[(currentRow, currentCol)] = bestCost

        return bestCost


# Editorial solution:
class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        cost = 0 

        if startPos[0] < homePos[0]:
            for row in range(startPos[0] + 1, homePos[0] + 1):
                cost += rowCosts[row]
        else:
            for row in range(startPos[0] - 1, homePos[0] -1, -1):
                cost += rowCosts[row]

        if startPos[1] < homePos[1]:
            for col in range(startPos[1] +1, homePos[1] +1):
                cost += colCosts[col]
        else:
            for col in range(startPos[1] - 1, homePos[1] -1, -1):
                cost += colCosts[col]

        return cost
        