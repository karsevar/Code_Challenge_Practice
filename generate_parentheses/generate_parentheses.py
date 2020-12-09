class Solution:
    def generateParenthesis(self, n):
        
        # will need to create a recursion function that will help with the 
        # different combinations required to create well formed arrays.
        
        # in addition I will need to think about the characteristic of the problem 
        # where n = 3 and three opening parentheses and closing parentheses are 
        # factored into the combinations. I believe this means that I can have 
        # two separate arrays one containing opening parentheses and one containing
        # closing parentheses.
        
        length = n * 2
        combinations = []
        
        def recursion_helper(length, n, opening=0, closing=0,  combination=''):
            if length == len(combination):
                stack = []
                stack.append(combination[0])
                balanced_boolean = True
                
                if combination[0] == ')':
                    balanced_boolean = False
                else:
                    for bracket in combination[1:]:
                        if bracket == '(':
                            stack.append(bracket)
                        elif bracket == ')':
                            if len(stack) != 0:
                                stack.pop() 
                            else:
                                balanced_boolean = False
                        
                if len(stack) == 0 and balanced_boolean:
                    combinations.append(combination)
            elif length > len(combination):
                if n > opening:
                    recursion_helper(length, n, opening+1, closing, combination+'(')
                if n > closing:
                    recursion_helper(length, n, opening, closing - 1, combination + ')')
                    
        recursion_helper(length, n)
        return combinations