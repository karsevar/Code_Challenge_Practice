class Solution:
    # quick solution using bruteforce. 
    # in place of worrying about the results array in the recursion function I instead separated the logic for the count within the recursion function and the collection of counts within the results array output in the parent function. 
    # in all I believe that the time complexity can be calculated at O(n^n*s) given that I'm looping through a matrix of size n*n and I'm calculating the possible move count using the len of the input s string.
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # okay this is an interesting problem. To begin, I think that the R, D, U, L instructions should be placed within an array that has the strings as keys. example directions = {"R": 1, "L": -1, "d": 1, "U": -1}
        # base case is if the the robot is directed out of the matrix or you reach the end of the instruction list. 
        # We will need to count the number of moves the robot can make before going out of bounds and iterate over the s string throughout the recursion loop.
        # the answer array will be the same length of the input s string. 
        # n is the dimensions of the matrix.

        # create a recursion function that will take n (dimension of the matrix), j (column index), i (row index), s_index (perhaps we might need to keep track of the string index we are currently assessing in the loop), s.

        results = []

        for s_index in range(len(s)):
            current_count = self.recursion_helper(
                startPos[0],
                startPos[1],
                0,
                n,
                s_index,
                s,
            )
            results.append(current_count)

        return results

    def recursion_helper(self, j: int, i: int, count: int, n: int, s_index: int, s: str) -> int:
        move_dict = {
            "L": -1,
            "R": 1,
            "D": 1,
            "U": -1,
        }

        results = []

        if j >= n or j < 0 or i >= n or i < 0:
            return count-1 if count > 0 else 0
        if s_index == len(s):
            return count

        move = move_dict[s[s_index]]

        return self.recursion_helper(
            j + move if s[s_index] == "U" or s[s_index] == "D" else j,
            i + move if s[s_index] == "L" or s[s_index] == "R" else i,
            count+1,
            n,
            s_index+1,
            s,
        )