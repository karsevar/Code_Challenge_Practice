## First attempt not really optimized since I'm still going through all the possible states and I'm simply looping
# through the state array to find if the number (choice) is already represented in the state array. 
# this solution passes up to 9 out of 10 test cases. 

# according to the editorial the best and most time efficient solution is to use the index of the choice in question
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        print("nums: ", nums) 
        # So in order to solve these specific problems I will need to think in terms of using the backtrack recursion method meaning that I will need to recursively check each decision within the tree to find whether it's true or not. 
        # For this problem the base case will be if a specific subset is not in the solutions array already. And the is valid state will be used to check if the selection is already in the solution array as well.

        # I believe that the best way is to test out how recursion works and back track on how to formulate the base cases

        results = []
        self.backtrack_subsets([], nums, results)

        # print("results: ", results)
        return results



    def backtrack_subsets(self, state, options, results):
        # print("options: ", options, " state: ", state, " results: ", results)
        state_sorted = sorted(state.copy())

        if state_sorted not in results:
            results.append(state_sorted)
        
        for choice in options:
            if choice not in state:
                # print("choice: ", choice, " state: ", state)
                state.append(choice)

                self.backtrack_subsets(state, options, results)

                state.pop()