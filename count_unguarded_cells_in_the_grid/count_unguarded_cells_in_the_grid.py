class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        # okay so the hints are telling me to simply create the matrix from scratch and document all of the visited tiles then iterate over the matrix again and count the number of tiles that weren't visited by the guards or are not walls

        # create the matrix
        matrix = [[0] * n for _ in range(m)]

        # create a moves array that will have the up, down left, right moves a guard can make.

        # so we can iterate through the guard array and use their index positions as the starting position for each initial call of the recursion function.
        # create another loop that will iterate through all the moves the guard can make in order
        # the recursion function will be used to actively modify the in matrix with all the tiles that were visited. All the visited tiles will be marked as 1 included the walls.

        for row, col in guards:
            matrix[row][col] = 1

        for row, col in walls:
            matrix[row][col] = 2

        guard_moves = {
            # up
            (-1, 0),
            # down 
            (1, 0),
            # left 
            (0, -1),
            # right
            (0, 1),
        }
        
        for guard in guards:
            for move in guard_moves:
                self.recursion_helper(
                    guard[0]+move[0],
                    guard[1]+move[1],
                    move,
                    matrix,
                )
        
        count = 0
        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[j][i] == 0:
                    count += 1

        return count

    def recursion_helper(self, j: int, i: int, move: tuple[int], matrix: List[List[int]]):
            if j >= len(matrix) or j < 0 or i >= len(matrix[0]) or i < 0:
                return

            if matrix[j][i] == 1 or matrix[j][i] == 2:
                return

            matrix[j][i] = 3
            self.recursion_helper(
                j+move[0],
                i+move[1],
                move,
                matrix,
            )

            
