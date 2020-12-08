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