# The time complexity of this solution will be O(n^k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # this problem seems to be very similar to the subsets problem with the exception being that I'm only given n to create the subset array in place of a nums array and in addition the constraint is 1 to 20. This means that each number value will be unique and from the example solutions it seems that we don't need to include an empty array.

        # also it seems that k is used to limit the size of the array results.

        # of course create a results array that will be passed into a helper recursive function
        results = []

        # create options array
        options = [i for i in range(1, n + 1)]

        # create recursive function that will take in n options and results as arguments
        self.backtrack_helper(k, options, [], results)

        # return results
        # print("results: ", results)
        return results

    def backtrack_helper(self, k: int, options: List[int], state, results):
        # base case check if current state is length equal to k
        # if so add a copy of the state to the results array 

        # create for loop that will loop through options values
        # add option index value to state
        # call backtrack helper function
        # remove included value from state

        # print("options: ", options, " state: ", " results: ", results)

        if len(state) == k:
            results.append(state[:])
            return 

        for choice in options:
            if len(state) == 0:
                state.append(choice) 
                self.backtrack_helper(k, options, state, results)
                state.pop()
            elif len(state) != 0 and state[-1] < choice:
                state.append(choice) 
                self.backtrack_helper(k, options, state, results)
                state.pop()


# created this solution through looking through the solutions for this specific question and combining to 
# loop logic from a subsets solution post. Will need to understand why we need to call self.dfs() 
# after subset.pop() in order to explore the remaining choices.
class SolutionEditorial1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        self.dfs(n, k, 1, [], ans)

        return ans

    def dfs(self, n: int, k: int, i: int, subset: List[int], ans: List[List[int]]):
        if len(subset) == k:
            ans.append(subset[:])
            return 
        
        if i <= n:
            subset.append(i)
            self.dfs(n, k, i + 1, subset, ans)
            subset.pop() 
            self.dfs(n, k, i + 1, subset, ans)


# A little more interesting solution. It seems that the dfs(i+1) call is used to remove the possibility 
# of duplicate values within the ans array. Very interesting solution.
class SolutionEditorial2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(start):
            if len(subset) == k:
                ans.append(subset[:])
                return 

            for i in range(start, n + 1):
                subset.append(i)
                dfs(i + 1)
                subset.pop()

        dfs(1)
        return ans
        