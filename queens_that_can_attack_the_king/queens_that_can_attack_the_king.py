class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # read some of the suggestions with this problem initially I was thinking of using the queens to find if they can attack the king and have conditionals that will remove possible queens through either them not being in range of a king or are obstructed by another queen.
    # from reading the editorial I found that you can actually use the king's position to find all the possible queens that can attack. In addition, I wrongly had the moves dictionary in the recursion function which caused the recursion to timeout due to queens only being able to move in one direction when making a single move.
    # time complexity might be O(n*m) since in the worst case I am exploring the entire matrix.
        results = []

        moves_dict = {
            # up
            (-1, 0),
            # up left
            (-1, -1),
            # up right
            (-1, 1),
            # right 
            (0, 1),
            # left 
            (0, -1),
            # down
            (1, 0),
            # down left
            (1, -1),
            # down right
            (1, 1),
        }

        for direction in moves_dict:
            self.recursion_helper(
                king[0],
                king[1],
                queens,
                results,
                direction,
            )

        return results



    def recursion_helper(self, king_j: int, king_i: int, queens: list[list[int]], results: list[list[int]], move: tuple[int]):
        if king_j >= 8 or king_i >= 8 or king_i < 0 or king_j < 0:
            return 
        if [king_j, king_i] in queens:
            results.append([king_j, king_i])
            return 

        self.recursion_helper(
            king_j + move[0],
            king_i + move[1],
            queens,
            results,
            move,
        )