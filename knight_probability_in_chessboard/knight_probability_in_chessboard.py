class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Okay so much like the other grid problems we need to create recursive calls that will encompass all possible movements of the knight which has a total of eight different movements.
        # base case will be if k is equal to zero 
        # if the knight is still in the grid than return 1
        # if the knight is outside of the grid than return 0

        # we will need to return the probability calculation so return possible paths/8^k 

        cache = {}
        return self.recursionHelper(
            column,
            row,
            k,
            n,
            cache,
        ) / 8**k

    def recursionHelper(self, j: int, i: int, k: int, n: int, cache: dict[tuple[int], int]) -> int:
        if (j >= n or i >= n or j < 0 or i < 0):
            return 0
        elif j < n and i < n and j >= 0 and i >= 0 and k == 0:
            return 1

        if (j, i, k) in cache:
            return cache[(j, i, k)]

        # moves
        moves = [
            #up left and right
            (-2, -1),
            (-2, 1),
            # down left and right
            (2, -1),
            (2, 1),
            # left down and up
            (-1, -2),
            (1, -2),
            # right down and up
            (-1, 2),
            (1, 2),
        ]

        moveCount = 0 
        for move in moves:
            moveCount += self.recursionHelper(
                j+move[0],
                i+move[1],
                k-1,
                n,
                cache,
            )

        cache[(j, i, k)] = moveCount
        return cache[(j, i, k)]