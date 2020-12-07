# Unable to pass almost all of the test cases with this implementation. The 
# only edge cases that this solution can solve is if the original substring 
# is not a palindrom. 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # create a variable that will carry the highest length 
        # count of a palindrome in the string
        solutions = []
        
        def recursion_helper(string, solutions):
            if len(string) == 1:
                return string
            elif len(string) > 1:
                isEven = None
                if len(string) % 2 == 0:
                    midpoint = len(string) // 2
                    left_string = string[:midpoint]
                    isEven = True
                else:
                    midpoint = (len(string) // 2) + 1
                    left_string = string[:midpoint-1]
                    isEven = False

                right_reversed = ''

                for character in range(len(string)-1, midpoint-1, -1):
                    right_reversed += string[character]
                    
                if right_reversed == left_string:
                    return string 
                else:
                    left_values = recursion_helper(string[1:], solutions)
                    if left_values != None:
                        solutions.append(left_values)
                    right_values = recursion_helper(string[:-1], solutions)
                    if right_values != None:
                        solutions.append(right_values)
              
        if len(s) > 3:  
            recursion_helper(s, solutions)
            highest_count = ''

            for solution in solutions:
                if len(highest_count) < len(solution):
                    highest_count = solution
                    
            print('solutions', solutions)
            
            return highest_count
        elif len(s) == 1:
            return s
        elif len(s) == 2:
            if s[1] == s[0]:
                return s
            else:
                return s[1]
        elif len(s) == 3:
            if s[1] == s[-1]:
                return s
            else:
                return s[1]

# was forced to get this solution from a youtube video: link: https://www.youtube.com/watch?v=IrD8MA054vA     
class SolutionVideo:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
                # print('palindrome substrings', s[l+1:r])
            
            return s[l+1:r]
        
        res = ''
        for i in range(len(s)):
            test = helper(i,i)
            if len(test) > len(res): 
                res = test 
            
            test = helper(i, i+1)
            if len(test) > len(res):
                res = test
                
        return res