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