# Bruteforce method with no optimizations only passes 23 of the 176 test cases. Due to the way the recursion is 
# set up I'm processing the same combinations as well as I'm re-summing the state with each iteration of the 
# recursion loop.
class SolutionBruteForce:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # window method will probably won't work for this particular problem because I need to find all possible combinations that will equal to a specific target. This is pretty much a backtracking algorithm problem though most likely I will need to think about possible optimizations since candidate length can go up to 100 and factorial time complexity will hit the efficiency window at candidate array length of 10.

        # As stated above the best solution is the backtracking dfs approach.

        # create a solutions array

        # create a function that will take in candidates, target, state, choice as an index integer (this will make sure that we will not count the same index twice)

        # return solutions array

        solutions =[]
        n = len(candidates)

        self.backtrack_helper(candidates, 0, n, target, [], solutions)

        # print("solutions: ", solutions)

        return solutions

    def backtrack_helper(self, candidates: List[int], choice: int, n: int, target: int, state: List[int], solutions: List[List[int]]):
        # base case: Check if target equals 0.
        # create a nested conditional that checks if i is less than len(candidates)
        # if true add state copy of state to the solutions array 
        # if target is less than zero return nothing
        # append candidates[choice] to the state array
        # call backtrack_helper with updated state array and target - candidates[choice] as well as with all the other arguments
        # pop final value from state
        state_sum = sum(state)
        # print(" outside conditional state: ", state, " target: ", target, " choice: ", choice, " state_sum: ", state_sum)
            
        if target == state_sum:
            state_sorted = sorted(state[:])
            if state_sorted not in solutions:
                solutions.append(state_sorted)
                return
        elif target > state_sum and choice < n:
            state.append(candidates[choice])
            self.backtrack_helper(candidates, choice + 1, n, target, state, solutions)
            state.pop()
            self.backtrack_helper(candidates, choice + 1, n, target, state, solutions)


# Through this solution I was able to go up to 171 out of 176 test cases through optimizing the additional logic
# The final couple of test cases were fixed through referring to the editorial section of the challenge since 
# through my loop I was getting duplicates and as a means to fix the duplicates problem I was forced to loop through 
# the solutions array to check if the combinations are truely unique. 
# time complexity is O(2^n * k)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # window method will probably won't work for this particular problem because I need to find all possible combinations that will equal to a specific target. This is pretty much a backtracking algorithm problem though most likely I will need to think about possible optimizations since candidate length can go up to 100 and factorial time complexity will hit the efficiency window at candidate array length of 10.

        # As stated above the best solution is the backtracking dfs approach.

        # create a solutions array

        # create a function that will take in candidates, target, state, choice as an index integer (this will make sure that we will not count the same index twice)

        # return solutions array

        solutions =[]
        candidates = sorted(candidates)
        n = len(candidates)

        self.backtrack_helper(candidates, 0, n, target, [], solutions)

        # print("solutions: ", solutions)

        return solutions

    def backtrack_helper(self, candidates: List[int], choice: int, n: int, target: int, state: List[int], solutions: List[List[int]]):
        # base case: Check if target equals 0.
        # create a nested conditional that checks if i is less than len(candidates)
        # if true add state copy of state to the solutions array 
        # if target is less than zero return nothing
        # append candidates[choice] to the state array
        # call backtrack_helper with updated state array and target - candidates[choice] as well as with all the other arguments
        # pop final value from state
        # state_sum = sum(state)
        # print(" outside conditional state: ", state, " target: ", target, " choice: ", choice)
            
        if target == 0:
            solutions.append(state[:])
            return
        elif target > 0 and choice < n:
            state.append(candidates[choice])
            self.backtrack_helper(candidates, choice + 1, n, target - candidates[choice], state, solutions)
            state.pop()
            while choice + 1 < n and candidates[choice] == candidates[choice + 1]:
                choice += 1
            self.backtrack_helper(candidates, choice + 1, n, target, state, solutions)