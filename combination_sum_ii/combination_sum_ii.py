# first try solution with not the best time complexity.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # make sure to sort the input candidates array first 
        
        # create a recursive function that will take the candidates array, the 
        # target, and combinations array that will be initialized to None 
            # base case:
                # if target equals zero then add combination to combinations array
            # recursive case:
                # if target is less than zero recursively call the function through 
                # a for loop
        candidates.sort()
        visited = set()
        combinations = []
                
        def recursion_helper(candidates, start, target, combination=None):
            if target == 0:
                if tuple(combination) not in visited:
                    visited.add(tuple(combination))
                    combinations.append(combination)
            elif (target > 0):
                for num in range(start, len(candidates)):
                    if combination == None:
                        newCombination = [candidates[num]]
                    else:
                        newCombination = combination[:]
                        newCombination.append(candidates[num])
                        
                    recursion_helper(candidates, num + 1, target-candidates[num], newCombination)
                
        recursion_helper(candidates, 0, target)
        return combinations