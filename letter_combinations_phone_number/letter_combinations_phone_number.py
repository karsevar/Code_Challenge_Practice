class Solution:
    def letterCombinations(self, digits):
        # create a number to letter dictionary that will contain a 
        # number with an array of corresponding letters 
        
        # create a recursive helper function that will be used to 
        # loop through each individual digit and print a possible 
        # letter combination 
            # base case:
                # if combination is the same length as digits 
                    # append combination to combinations array 
                    
            # recursive case:
                # if combination is not the same length as digits 
                    # recursively call the recursive helper function 
                    
                    
        number_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        if len(digits) == 0:
            return []
        
        combinations = []
        
        digits_length = len(digits)
        
        def recursive_helper(digits_length, digits, combination=''):
            if digits_length == len(combination):
                combinations.append(combination)
                
            elif digits_length > len(combination):
                for begin_letter in number_map[digits[0]]:
                    new_combination = combination 
                    new_combination += begin_letter
                    
                    recursive_helper(digits_length, digits[1:], new_combination)
                    
                    
        recursive_helper(digits_length, digits)
        
        return combinations