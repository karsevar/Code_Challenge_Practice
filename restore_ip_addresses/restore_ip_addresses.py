class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # the most straightforward way to reason about this problem is to think of s as some kind of queue or stack where we look at the indexes in three digit increments and see if they fullfill specific invalidation rules. 
            # is the three digit increments an actual number?
            # is the number between 0 and 255

        # if they pass these validation principles than we can add them to the state array.

        # base case will be if the state array matches a length of four.

        # recursive case will be if the state array is less than the length of four.

        # create a results array
        # create a recursive function that will take state, s, results as arguments

        # return results

        results = []
        self.recursive_helper([], s, results)
        return results

    def recursive_helper(self, state: List[str], s: str, results: List[List[str]]):
        # base case if the state variable has a length equal to 4 than add it to the results array. Make sure that the state variable is converted to a string with a . delimiter.

        # recursive case
        # if the state variable has a length variable less than 4.
            # create a for loop that will loop through three digit spots of the s variable 
                # create a conditional check to see if s[:i] are valid ip address integers.
                    # if true add s[:i] to the state array
                    # recursively call recursive_helper with updated state array, s[:i+1], and results array
                    # deselect s[:i] in the state array

        if len(state) == 4 and len(s) == 0:
            state_str = ".".join(state[:])
            results.append(state_str)
            return 
        elif len(state) < 4 and len(s) > 0:
            for i in range(1, 4):
                if i > len(s):
                    break
                
                if self.ip_digit_validator(s[0:i]):
                    state.append(s[0:i])
                    self.recursive_helper(state, s[i:], results)
                    state.pop()

    def ip_digit_validator(self, digit: str) -> bool:
        if digit[0] == "0" and len(digit) > 1:
            return False
        if int(digit) <= 255:
            return True
        
        return False