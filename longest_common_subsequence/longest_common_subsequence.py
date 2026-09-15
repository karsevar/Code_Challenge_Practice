class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # This problem can be thought of as a 2D dynamic programming problem since we are effectively keeping track of two indexes. text1[i] and text2[j]. I believe that much like the robot moving in a grid problem, we can think of this one as either we can move i or j one index spaces at a time. 
        # base case can be interpreted as if text1[i] == text[j] then we return 1. The issue with the basic return 1 base case is that we need to keep iterating over both strings until we reach the last indexes.

        cache = {}

        return self.recursionHelper(
            0,
            0,
            text1,
            text2,
            cache,
        )


    def recursionHelper(self, i: int, j: int, text1: str, text2: str, cache: dict[tuple[int], int]) -> int:
        if i >= len(text1) or j >= len(text2):
            return 0 

        if (i, j) in cache:
            return cache[(i, j)]

        if text1[i] == text2[j]:
            return 1 + self.recursionHelper(
                i+1,
                j+1,
                text1,
                text2,
                cache
            )
        else:
            move_i = self.recursionHelper(
                i+1,
                j,
                text1,
                text2,
                cache
            )

            move_j = self.recursionHelper(
                i,
                j+1,
                text1,
                text2,
                cache
            )

            cache[(i, j)] = max(move_i, move_j)
            return cache[(i, j)]