class Solution:
    # not really the most straightforward solution since I'm simply using a recursion function to loop through the board for each of the four different moves that a rook can make in chess. This same solution can be simplified into using simply a while loop. 
    # Logically I believe that the time complexity can be interpreted as O(n*m) since we are looping through technically every column and row of the chess board matrix.
    def numRookCaptures(self, board: list[list[str]]) -> int:
        # So in total the rook can only attack a maximum of 4 pawns. so the answers can range between 0 to 4. In addition, the most straightforward way is to think of this as some kind of a dynamic programming problem where I can simply have the rook move in a single direction until it encounters a pawn or another piece. If it encounters a pawn then we can return 1 if it encounters a different piece or the end of the matrix we return 0.

        # first we will need to loop through the matrix and find the location of the rook piece 
        rook_location = () # will contain the location of the rook piece using j and i indexes.

        for j in range(len(board)):
            for i in range(len(board[0])):
                if board[j][i] == "R":
                    rook_location = (j, i)

        rook_moves = {
            # down
            (1, 0),
            # up 
            (-1, 0),
            # left
            (0, -1),
            # right 
            (0, 1)
        }

        pawn_count = 0
        for move in rook_moves:
            pawn_count += self.recursion_helper(
                rook_location[0]+move[0],
                rook_location[1]+move[1],
                move,
                board,
            )

        return pawn_count

    def recursion_helper(self, j: int, i: int, move: tuple[int], board: list[list[int]]) -> int:
        if j >= len(board) or j < 0 or i >= len(board[0]) or i < 0:
            return 0
        if board[j][i] == "p":
            return 1
        if board[j][i] != "." and board[j][i] != "p":
            return 0

        count = 0

        count += self.recursion_helper(
            j+move[0],
            i+move[1],
            move,
            board,
        )

        return count
