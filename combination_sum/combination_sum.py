class Solution:
    def combinationSum(self, candidates, target):
        # create a recursion helper function that will be used to 
        # recursively step through the list and see what combinations 
        # create the target value 
            # base cases:
                # if minus amount is less than the target 
                # if minus amount is equal to the target 
                
            # recursive case 
                # loop through the candidates array 
                    # recursively call the recursion helper function 
                    # on each value in the loop
                    
        visited = set()
        combinations = []
                    
        def recursion_helper(candidates, target, combination=None):
            if target == 0:
                combination.sort()
                visited_cell = tuple(combination)
                if visited_cell not in visited:
                    print("combination found", combination)
                    visited.add(visited_cell)
                    combinations.append(combination)
            if target < 0:
                return None 
            else:
                for value in candidates:
                    if combination == None:
                        cur_combination = [value]
                    else:
                        cur_combination = combination[:]
                        cur_combination.append(value)
                        
                    recursion_helper(candidates, target - value, cur_combination)
                    
        recursion_helper(candidates, target)
        return combinations
    

class SolutionRevisited:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # I can most likely solve this problem using almost the same logic as combination sum ii with the main difference being that I'm able to count the same number multiple times. 

        # create a solutions array

        # create a function that will candidates, target, state, and solutions as arguments.

        # return solutions array

        solutions = []

        self.backtrack_helper(candidates, target, solutions, [])

        return solutions


    def backtrack_helper(self, candidates: List[int], target: int, solutions: List[List[int]], state: List[int]):
        # base case: 
        ## Check if target equals zero (each iteration of the recursion loop will effectively subtract candidates[choice] from the running target value)
        ## if true add state to the solutions array
        ## if less than target
        ### create a for loop that through the candidates array
        ### add candidate[choice] to state
        ### call backtrack_helper with updated state and updated target (target - candidates[choice])
        ### pop candidate[choice] from bottom of the state array

        if target == 0:
            sorted_state = sorted(state[:])
            if sorted_state not in solutions:
                solutions.append(sorted_state)
            return

        elif target > 0:
            for choice in candidates:
                state.append(choice)
                self.backtrack_helper(candidates, target - choice, solutions, state)
                state.pop()


class SolutionWithCache:
    # not the most efficient solution as it only beats 5 percent of all submissions. The inefficiency is due to not cache all the possible paths that the algorithm processed thus we are revisited paths that have already been explored. 

    # easy fix is to use a set as a cache for previously visited paths in order to decrease time complexity.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # to begin I will use the same principles as the other backtrack problems where the following pattern is utilized.
        # for loop through the choices in the candidates array
        # add choice to state array
        # call recursive function with updated state
        # remove choice from state

        # what should the conditional be within the base case?
        # To start the unoptimized version of this algorith would be to add state and check if it equals target or is greater than the target.

        # visited set
        # example of visited set: set(" ", "1 2")


        results = []
        # this modification did speed the algorithm up to 95 ms from 2000 ms. Though the time complexity is not at the same level as some of the other submissions.
        visited = set()
        self.combination_sum_helper(visited, [], candidates, target, results)

        return results

    def combination_sum_helper(self, visited, state, candidates, target, results):
        # print("state: ", state, " target: ", target, " results: ", results, " visited: ", visited)
        sorted_state = sorted(state[:])
        str_state = str(sorted_state)

        if str_state not in visited:
            visited.add(str_state)
            if target < 0:
                return
            if target == 0:
                results.append(sorted_state)
                return

            for choice in candidates:
                state.append(choice)
                self.combination_sum_helper(visited,state, candidates, target - choice, results)
                state.pop()