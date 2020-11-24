def alternatingCharacters(s):
    # if s is length one or zero return the length of s

    # create a counter that will count the number of times the current 
    # character is the same as the current character 
    
    # create a for loop that will increment through the string starting at the 
    # 1 index 
        # if the current character and the past character are the same increment 
        # the counter by one
        
    print('string', s)
    
    if len(s) == 1 or len(s) == 0:
        return len(s) 
    else:
        similar_count = 0 
        
        for current_index in range(1, len(s)):
            if s[current_index - 1] == s[current_index]:
                similar_count += 1
                
        return similar_count