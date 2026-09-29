class SolutionFirstAttempt:
    # uses a modification of fixed window. 
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # I believe that perhaps we can do the iterative approach without having to use dynamic programming and recursion persay. 
        # constraints to consider is that the s string will need to always be equal to or greater than the size of all the combined words in the input wordDict array. 
        # this might require additional processing where we "".join(wordDict) and check if it's equal to or greater than the size of s.
        # In addition, we can perhaps split the s string and each individual words in the wordDict array into arrays with letters.

        # the iterative mechanism can be an outer for loop that will loop through wordDict 
        # and an inner for loop that will loop through the input s string for i in range(len(word) - 1)
        # create a conditional if s[i:len(word)] == word and find a way to document the index positions that should be removed from the string. 
        # false conditional will mean the s string still has letters

        # documenting the index positions (start index, end index+1)

        # now I understand what I'm doing wrong it seems that this method is a little too rigged when it comes to the order in which the words are placed in wordDict. It might be a little too complex to continue modifying this method. The test case in which this solution is failing is 36.
        # time complexity is O(WD * S) where s is the input string and WD is the input word dictionary.

        for word in wordDict:
            index_positions = []
            if len(s) == 0:
                break
            for i in range(len(s) - len(word) + 1):
                if word == s[i:i + len(word)]:
                    index_positions.append((i, i + len(word)))

            for index_position in reversed(index_positions):
                s = s[:index_position[0]] + s[index_position[1]:]

        return len(s) == 0


class SolutionDynamicProgramming:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Dynamic programming approach using tabulation.

        dp = [False] *  (len(s) +1)

        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] is False:
                    continue

                substring = s[j:i]

                if substring in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]