# was able to solve this using a modified version of the combination sum ii pattern. I believe that the time complexity 
# might be the same as that solution as well. The same issue with this solution is that I'm having a little 
# trouble reasoning about how the skipping duplicates logic works as well as the second declaration of the 
# recursion helper. Perhaps the second declaration is used to process the other subsets after deselecting 
# choice from the state array. Will need to experiment a little more with these problems.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # okay for this subset problem I can use the same logic as subsets problem one with the added caveat of having to filter through the duplicate subsets.

        # first I will setup to the same logic as the previous problem.
        
        # sort the nums array (this will help with the duplicate logic later on).

        # create a solutions array

        # create a backtrack_helper function that will have the following for arguments.
        ## nums, choice (the index for the value that will be included in state), state, and solutions

        # return the solutions array

        nums = sorted(nums)

        solutions = []
        self.backtrack_helper(len(nums), 0, nums, [], solutions)

        return solutions


    def backtrack_helper(self, n: int, choice: int, nums: List[int], state: List[int], solutions: List[List[int]]):
        # base case: since we want to process all the possible combinations of nums, we will need to get the first power set of the passed in array which is nums == nums
        # to get this the beginning base case will be choice == n 
        # we will append copy of state to solutions 

        # append nums[choice] to state
        # call backtrack_helper with updated state and choice + 1 value
        # unselect choice from state 
        # call backtrack_helper with updated state and choice + 1 value

        if n == choice:
            solutions.append(state[:])
            return 

        state.append(nums[choice])
        self.backtrack_helper(n, choice + 1, nums, state, solutions)
        state.pop()
        while choice + 1 < n and nums[choice] == nums[choice + 1]:
            choice += 1
        self.backtrack_helper(n, choice + 1, nums, state, solutions)


## Time complexity O(2^n * n)
class SolutionWithForLoop:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # okay for this subset problem I can use the same logic as subsets problem one with the added caveat of having to filter through the duplicate subsets.

        # first I will setup to the same logic as the previous problem.
        
        # sort the nums array (this will help with the duplicate logic later on).

        # create a solutions array

        # create a backtrack_helper function that will have the following for arguments.
        ## nums, choice (the index for the value that will be included in state), state, and solutions

        # return the solutions array

        nums = sorted(nums)

        solutions = []
        self.backtrack_helper(len(nums), 0, nums, [], solutions)

        return solutions


    def backtrack_helper(self, n: int, choice: int, nums: List[int], state: List[int], solutions: List[List[int]]):
        # base case: since we want to process all the possible combinations of nums, we will need to get the first power set of the passed in array which is nums == nums
        # to get this the beginning base case will be choice == n 
        # we will append copy of state to solutions 

        # append nums[choice] to state
        # call backtrack_helper with updated state and choice + 1 value
        # unselect choice from state 
        # call backtrack_helper with updated state and choice + 1 value

        solutions.append(state[:])

        for i in range(choice, n):
            if i != choice and nums[i] == nums[i - 1]:
                continue
            state.append(nums[i])
            self.backtrack_helper(n, i + 1, nums, state, solutions)
            state.pop()