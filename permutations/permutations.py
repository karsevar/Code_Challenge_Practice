# First attempt most test cases didn't pass. Perhaps I miss read the permutation 
# requirements for this problem.
class Solution:
    def permute(self, nums):
        
        # create a permutations array that will hold all the possible 
        # permutations 
        
        # create a recursive function that will have a start argument, nums argument,
        # and a permutation argument 
            # if permutation is equal to the length len(nums) and not none 
                # add permutation to the permutations array 
            # if permutation is less than the lenght of len(nums) 
                # have a for loop that will start at range(start, len(nums) + 1)
                    # recursively call the recursive function 
                    
        permutations = []
        nums_length = len(nums)
        
        def permutation_helper(nums, nums_length, permutation=None, variable_exclude=None):
            if permutation != None and len(permutation) == nums_length:
                permutations.append(permutation)
            elif permutation == None or len(permutation) < nums_length:
                for number in nums:
                    if permutation == None:
                        new_permutation = []
                        variable_exclude = number
                        new_permutation.append(number) 
                        permutation_helper(nums, nums_length, new_permutation, variable_exclude)
                    elif permutation != None and variable_exclude != number and number != permutation[-1]:
                        new_permutation = permutation[:]
                        new_permutation.append(number) 
                        permutation_helper(nums, nums_length, new_permutation, variable_exclude)
                    
        permutation_helper(nums, nums_length)
        return permutations 


class OfficialSolution:
    def permute(self, nums):
        
        # create a permutations array that will hold all the possible 
        # permutations 
        
        # create a recursive function that will have a start argument, nums argument,
        # and a permutation argument 
            # if permutation is equal to the length len(nums) and not none 
                # add permutation to the permutations array 
            # if permutation is less than the lenght of len(nums) 
                # have a for loop that will start at range(start, len(nums) + 1)
                    # recursively call the recursive function 
                    
        permutations = []
        nums_length = len(nums)
        
        def permutation_helper(index, perm, nums_length):
            if index == len(perm):
                permutations.append(list(perm))
            
            for i in range(index, len(perm)):
                print('permutation', perm)
                print('index', index)
                perm[index], perm[i] = perm[i], perm[index]
                permutation_helper(index+1, perm, nums_length)
                perm[index], perm[i] = perm[i], perm[index]
                
            
                    
        permutation_helper(0, nums, nums_length)
        return permutations 