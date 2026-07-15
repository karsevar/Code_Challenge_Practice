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


class SolutionWithCache:
    # it seems that I didn't have to use the i == i - 1 skip conditional in order to pass all of the test cases. Though this solution is the most optimal and I only used a path cache in order to pass the last 4 test cases. 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # in this case the values in the input candidates array are not unique. This means that I will need to keep track of the index position 

        # create a results array
        # create a recursion helper that will take start index, results, candidates, state, and target. I think I can decrease target with each index of candidate.
        # return results

        visited = set()
        results = []
        self.combination_helper([], 0, results, sorted(candidates), target, visited)
        return results

    def combination_helper(self, state: List[int], start: int, results: List[List[int]], candidates: List[int], target: int, visited):
        # base case will be if target is less than or equal to zero
        # if equal to zero add state to results array
        # if less than zero than just simply return null

        # create a for loop that will start at starting index and end at the length of the candidates array. 
        # Intition is that perhaps the loop will simply go through the array without repeating the same values in the computation state array.

        # add candidates[index] to state
        # recursively call combination_helper with index + 1 value and decrease target value by candidate[index]
        # print("start: ", start, " target: ", target, " results: ", results)
        state_copy = state[:]
        state_str = str(state_copy)

        if state_str not in visited:
            visited.add(state_str)
            if target == 0:
                results.append(state[:])
                return 
            if target < 0:
                return 

            for i in range(start, len(candidates)):
                state.append(candidates[i])
                self.combination_helper(state, i+1, results, candidates, target - candidates[i], visited)
                state.pop()


# This solution adds a conditional that prunes the decision tree so that we don't have to use a visisted 
# set as a cache to remove duplicate values. Now this solution beats 56 percent of submissions for time 
# complexity.
class SolutionTreePruneConditional:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.combination_helper([], 0, results, sorted(candidates), target)
        return results

    def combination_helper(self, state: List[int], start: int, results: List[List[int]], candidates: List[int], target: int):
        if target == 0:
            results.append(state[:])
            return 
        if target < 0:
            return 

        for i in range(start, len(candidates)):
            if (i > start and candidates[i] == candidates[i-1]):
                continue
            state.append(candidates[i])
            self.combination_helper(state, i+1, results, candidates, target - candidates[i])
            state.pop()