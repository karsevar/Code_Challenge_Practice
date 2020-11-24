def substrCount(n, s):
    print('n value', n) 
    print('s value', s)
    
    # create a substring_counter variable 
    # create a containing for loop that will iterate through the 
    # input string 
        # iterate counter by one 
        
        # create index counter initialized to current index 
        # create stack and add current index character in stack 
        # create is_middle boolean initialized to false
        
        # create while loop that will terminate once stack is empty or 
        # if next value is not the recurring value and is_middle is true 
            # iterate counter by one 
            # check if tail of stack is the same character as the next index 
                # if so add to stack and iterate counter by one 
                # if not change is_middle to true 
            # check if is_middle is true and if tail of the stack is the same as 
            # the next value 
                # if so pop from stack 
                    # if stack is empty after the pop iterate counter by one 
                # if not break  
                
    sub_counter = 0 
    
    for current_index in range(n):
        sub_counter += 1 
        
        inner_index = current_index 
        stack = []
        stack.append(s[inner_index])
        is_middle = False
        
        while inner_index != (n - 1):
            inner_index += 1
            if stack[-1] == s[inner_index] and is_middle == False:
                stack.append(s[inner_index])
                sub_counter += 1
            elif stack[-1] != s[inner_index] and is_middle == False:
                is_middle = True 
            elif is_middle == True:
                if stack[-1] == s[inner_index]:
                    stack.pop()
                    if len(stack) == 0:
                        sub_counter += 1
                        break
                else:
                    break
                
    return sub_counter  