class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # according to the sliding window solution I will need to have 
        # two pointers and a set that keeps track of the current state of the 
        # substring 
        
        # create a set() this will keep track of the current state of the 
        # substring and flag all duplicates that the loop runs into 
        # create a counter that will keep track of the largest substring 
        # in the loop 
        # create two pointers in total named left and right initialized to 
        # index zero 
        
        # create while loop that will end once the left pointer is at the 
        # last index of the input string 
            # iterate the left pointer by one index position 
            
            # if the strings at the left index is different from the right index
                # add the character to the set 
                # if not:
                    # create a new while loop that will continue to iterate once
                    # the duplicate character is deleted from the set
                    
        if len(s) == 0:
            return 0
        
        characters = set()
        left_pointer = 0
        right_pointer = 0 
        characters.add(s[left_pointer])
        counter = 1
        
        while right_pointer < len(s)-1:
            right_pointer += 1 
            
            if s[right_pointer] not in characters:
                characters.add(s[right_pointer])
                
                if len(characters) > counter:
                    counter = len(characters)
                    
            else:
                while True:
                    if left_pointer == right_pointer:
                        break 
                        
                    if s[left_pointer] == s[right_pointer]:
                        left_pointer += 1 
                        break
                    else:
                        characters.remove(s[left_pointer])
                        left_pointer += 1
                        
        return counter