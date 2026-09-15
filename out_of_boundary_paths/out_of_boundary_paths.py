class Solution:
    # This isn't really the best solution as I'm calling the recursion function four different times just to simulate the four possible directions that the ball can be kicked.
    # I think that perhaps the time complexity can be conceptualized as O(4n*m) Though I think that it might be a little worse than that due to the appearance of maxMove variable.
    # After implementing a cache the time complexity can be conceptualized as O(n*m*maxMove)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # not really sure if this is going to work but the main solution that I can think of simply calling a recursive function a total of four times corresponding to the different moves the ball can be kicked (right, left, down, and up).
        # maxMove will be used as a base case to remove extraneous paths.
        # an out of bound base case will only be counted if maxMove is not below zero and the ball is either out of bounds in the i index or j index
        # cases that will return zero will be when the ball is still in the grid and the maxMove count is zero.
        cache = {} # {(j, i, maxMove value) = count}
        return self.recursionHelper(
            startRow,
            startColumn,
            m,
            n,
            maxMove,
            cache,
        )

    def recursionHelper(self, j: int, i: int, m: int, n: int, maxMove: int, cache: dict[tuple[int], int]) -> int:
        if (j >= m or i >= n or i < 0 or j < 0) and maxMove >= 0:
            return 1
        if maxMove < 0:
            return 0

        if (j, i, maxMove) in cache:
            return cache[(j, i, maxMove)]

        rightMove = self.recursionHelper(
            j,
            i+1,
            m,
            n,
            maxMove-1,
            cache,
        )
        leftMove = self.recursionHelper(
            j,
            i-1,
            m,
            n,
            maxMove-1,
            cache,
        )
        downMove = self.recursionHelper(
            j+1,
            i,
            m,
            n,
            maxMove-1,
            cache,
        )
        upMove = self.recursionHelper(
            j-1,
            i,
            m,
            n,
            maxMove-1,
            cache,
        )

        cache[(j, i, maxMove)] = (rightMove + downMove + leftMove + upMove) % (10**9 + 7)
        return cache[(j, i, maxMove)]