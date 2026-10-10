class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        # the most straightforward way to solve this is through recursion. Will need to think up a way to test out different starting positions in the first row.

        # most likely the only the easiest way is to loop through the values in the first row and pick which path leads to the lowest sum. 

        # the number of possible moves is move down one row. or move diagonally to the right or left.
        # base cases will be if the current index position is out of bounds than return a large value. if the last row is reached return zero.

        # Bruteforce solution that only passes 37 of the 52 test cases. Time complexity is well beyond the dimensions of the input matrix array since I'm evaluating all possible min sums multiple times in the function. 
        # best way to solve for this is to add a cache that will take (i, j) index positions as a means to decrease time complexity.

        n = len(matrix)
        m = len(matrix[0])

        min_sum = float("inf")
        cache = {}

        for j in range(m):
            current_min = self.recursion_helper(
                matrix,
                0,
                j,
                cache,
            )
            min_sum = min(min_sum, current_min)

        return min_sum

    def recursion_helper(self, matrix: list[list[int]], i: int, j: int, cache: dict[tuple[int], int]) -> int:
        if j == len(matrix[0]) or j < 0:
            return float("inf")
        if i == len(matrix):
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        move_dict = {
            (1, 0), # move down
            (1, 1), # move diagonal right
            (1, -1), # move diagonal left
        }

        min_sum = float("inf")

        for move in move_dict:
            current_sum = matrix[i][j] + self.recursion_helper(
                matrix, 
                i+move[0],
                j+move[1],
                cache
            )
            min_sum = min(min_sum, current_sum)

        cache[(i, j)] = min_sum
        return cache[(i, j)]