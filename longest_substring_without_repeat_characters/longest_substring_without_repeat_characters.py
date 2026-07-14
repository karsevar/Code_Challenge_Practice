class Solution:
    def lengthOfLongestSubstringQueue(self, s: str) -> int:
        # I might be over complicating this problem. 
        # perhaps that most straightforward solution is to simply use the sliding window method where I can think of the substring as some kind of a queue where I can dequeue values that already exist in it and add values to increase the size of the queue. 
        # to keep a running max length I might have to find the size of the queue after each iteration of the loop. 
        # I believe that perhaps a single loop will be needed and possible optimizations can be made with letter lookup in the substring 

        # create a max substring length variable
        # create a substring value that will be initialized as ""
        # create a current length variable that will be initialized to zero

        # create a for loop that will loop through the entirety of s
        # create a conditional that will check if s[i] is in substring
        # if true remove value from the top of queue
        # add s[i] to the bottom of queue and check the length of the substring if substring length is greater than max length update max length

        # return max length

        # Okay for this solution we are only looping through the s string once so technically this algorithm can be regarding as o(n) and the space complexity can be o(n) since in the worst case the substring_queue can be the same size as the input string. 
        # The issue with this solution is that there are some inherent inefficiencies to consider when checking if a letter exists in an array of strings. This means that perhaps the time complexity for each look up in the conditional statement can give rise to O(n) as well.

        # Possible fix can be to simply keep track of the substring length of keep all the encountered letters in a set

        max_substring_length = 0
        current_substring_length = 0
        substring_queue = []

        for letter in range(len(s)):
            if s[letter] in substring_queue:
                while s[letter] in substring_queue:
                    substring_queue.pop(0)
            substring_queue.append(s[letter]) 

            if len(substring_queue) > max_substring_length:
                max_substring_length = len(substring_queue)

        return max_substring_length
    

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