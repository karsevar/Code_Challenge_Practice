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
    

# revisited algorithm:
class SolutionRevisted:
    def letterCombinations(self, digits: str) -> List[str]:
        # okay so the constrain is that we will only recieve numbers from 2-9 and that the length of digits will only be from 1 to 4.

        # the first course of action is to create a digit to letter hashmap that will be used to look up the letters each corresponding digit relates to. 

        # Perhaps the best idea is to first decode the digits to their possible letter and feed that into the recursive function but than that might make things more complicated.

        # create a results array that will contain the letter combinations

        # create a recursive function that will have the state, digits, and results as arguments. Will need to think about including index for a later time. 

        # return results

        self.letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.n = len(digits)

        results = []
        self.letter_recursion([], digits, results)
        return results


    def letter_recursion(self, state: List[str], digits: str, results: List[str]):
        # print("digits: ", digits, " state: ", state, " results: ", results)
        # base case will be if state has the same length as digits and is not in results add state to results

        # recursive case is:
        # create a for loop that will start at index 0 and end at len(digist) - 1
        # use digits[i] to get the possible letters from the hashtable
        # loop through possble letters and check if each letter is not already in state
        # if the letter is not in state add to state 
        # recursively call letter_recursion with updated state digits[i:]
        # pop letter from state array

        if self.n == len(state):
            state_string = "".join(state[:])
            if state_string not in results:
                results.append(state_string)
            return

        for digit in range(len(digits)):
            for letter in self.letter_map[digits[digit]]:
                state.append(letter)
                self.letter_recursion(state, digits[digit+1:], results)
                state.pop()