class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # this seems pretty much the same as combinationSum2 with the only exception being that we are given an integer to iterate over in a loop in place of being given an array.

        # the best first step is to use the same logic as must of these back track problems

        # create a results array

        # create a function that will be used for the recursion logic. Pass state, k and n and results as arguments. I seems that we don't need to worry about index. 

        # return results

        results = []
        self.combination_helper([], 1, k, n, results)
        return results

    def combination_helper(self, state, start, k, n, results):
        # base case: n is target so when the target is zero
            # append state in results
            # return null
        # if target is less than zero return null only

        # create a for loop that will start at one and end at n
        # append index value to state
        # recursively call combination_helper function
        # pop last value from state

        # print("state: ", state, " n: ", n, " results: ", results)

        if n == 0 and len(state) == k:
            results.append(state[:])
            return 
        if n < 0:
            return
        
        for i in range(start, 10):
            state.append(i)
            self.combination_helper(state, i+1, k, n - i, results)
            state.pop()