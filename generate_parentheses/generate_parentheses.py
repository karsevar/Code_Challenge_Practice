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
    

class SolutionRevisit:
    def generateParenthesis(self, n: int) -> List[str]:
        # okay so in order to solve this problem I will need to think in terms of closing and opening parentheses and the overall decision of picking either or.
        # the constraint is that n will only be up to 8.

        # I think I will need to create a limit counter for opening and closing parenteses.
        # If I choose a closing paretheses the limit will be decremented by one and if I choose an opening a parentheses I decrement that limit by one. 

        # create a results array
        # create a recursive function call that will take in opening_n and closing_n, state, and results as arguments.

        # return results

        results = []
        closing_n = n
        opening_n = n 
        self.n = n * 2

        self.generate_recursion([], closing_n, opening_n, results)
        return results

    def generate_recursion(self, state: List[str], closing_n: int, opening_n: int, results: List[str]):
        # base case if closing_n and opening_n are both zero adding state to results. Also will need conditional to check if state is already in results

        # create a for loop that will be n * 2
        # create a choice loop for either "(" or ")"
        # if opening_n is zero you can only choose closing parentheses 
        # adding parenthese choice to state
        # recursively call generate_recursion problem decrement opening or closing counters depending on the parentheses chosen
        # pop parenthese choice from state

        print("state: ", state, " closing_n: ", closing_n, " opening_n: ", opening_n, " results: ", results)

        if closing_n == 0 and opening_n == 0:
            state_str = "".join(state[:])
            if state_str not in results:
                results.append(state_str)
            return

        if opening_n > 0:
            state.append("(")
            self.generate_recursion(state, closing_n, opening_n - 1, results)
            state.pop()
        if closing_n > opening_n:
            state.append(")")
            self.generate_recursion(state, closing_n - 1, opening_n, results)
            state.pop()