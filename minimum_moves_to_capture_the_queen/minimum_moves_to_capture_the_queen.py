class SolutionSuboptimal:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # okay I believe that I can look at this problem as an offshoot of the minimum cost robot grid problem where we don't really need to explore the entire grid to find the optimal path. We only need to find out move the pieces in such a way that they can posibly capture the queen.
        # the possible moves for the rook is either up, down, left, right.
        # the possible moves for the bishop is diagonal left up, right up, down left, and down right. for the bishop we will need some kind of way to process if it can possibly reach the queen while the rook will be able to allows capture the queen due to it's move set.

        # we can create two different variables that will keep track of the moves for each piece.
        # rook_moves = 0
        # bishop_moves = 0

        # we can create separate loops for each piece.
        # for the rook.
        # if a < e move the rook down until it reaches the position of the queen.
        # if a > e move the rook up until it reaches the position of the queen

        # if b < f move the rook right until it reaches the position of the queen
        # if b > f move the rook right until it reaches the positoin of the queen

        # at the end of reach conditional statement rook moves will be incremented once

        # for the bishop
        # okay so for the bishop the coordinates need to be even or it is impossible for the piece to reach the queen 
        # so we need to create a separate check that finds out if the coordinates for both row and col if the queen are even if not then we don't need to move the bishop piece

        # basic MVP that passes initial test cases. Currently we are not checking if either piece is being obstructed or even if bishop needs to make more than one move.
        # This implementation is not passing the 541 test case due to me not adding logic that can handle processing if the bishop can capture the queen in two moves.
        # Was able to fix the logic for if either piece is obstructing the path to the queen.  

        rook_moves = 0
        bishop_moves = 0

        # bishop loop:
        if self.is_even(c) == self.is_even(e) and self.is_even(d) == self.is_even(f):
            current_bishop_row = c
            current_bishop_col = d

            if current_bishop_row < e and current_bishop_col < f:
                while current_bishop_row < e and current_bishop_col < f:
                    if current_bishop_row == a and current_bishop_col == b:
                        break
                    current_bishop_row += 1
                    current_bishop_col += 1
                bishop_moves += 1
                
            elif current_bishop_row > e and current_bishop_col > f:
                while current_bishop_row > e and current_bishop_col > f:
                    if current_bishop_row == a and current_bishop_col == b:
                        break
                    current_bishop_row -= 1
                    current_bishop_col -= 1
                bishop_moves += 1

            if current_bishop_row < e and current_bishop_col > f:
                while current_bishop_row < e and current_bishop_col > f:
                    if current_bishop_row == a and current_bishop_col == b:
                        break
                    current_bishop_row += 1
                    current_bishop_col -= 1
                bishop_moves += 1
            elif current_bishop_row > e and current_bishop_col < f:
                while current_bishop_row < e and current_bishop_col > f:
                    if current_bishop_row == a and current_bishop_col == b:
                        break
                    current_bishop_row -= 1
                    current_bishop_col += 1
                bishop_moves += 1

            if current_bishop_row == a and current_bishop_col == b:
                bishop_moves = float("inf")
        else:
            bishop_moves = float("inf")

        # rook loops:
        current_rook_row = a
        current_rook_col = b
        if current_rook_row < e:
            while current_rook_row < e:
                if current_rook_row == c and current_rook_col == d:
                    break
                current_rook_row += 1
            rook_moves += 1
        elif current_rook_row > e:
            while current_rook_row > e:
                if current_rook_row == c and current_rook_col == d:
                    break
                current_rook_row -= 1
            rook_moves += 1

        if current_rook_col < f:
            while current_rook_col < f:
                if current_rook_row == c and current_rook_col == d:
                    break
                current_rook_col += 1
            rook_moves += 1
        elif current_rook_col > f:
            while current_rook_col > f:
                if current_rook_row == c and current_rook_col == d:
                    break
                current_rook_col -= 1
            rook_moves += 1

        if current_rook_row == c and current_rook_col == d:
            rook_moves = float("inf")

        print("bishop moves: ", bishop_moves, " rook_moves: ", rook_moves)

        return min(rook_moves, bishop_moves)


    def is_even(self, num: int):
        return num % 2 == 0