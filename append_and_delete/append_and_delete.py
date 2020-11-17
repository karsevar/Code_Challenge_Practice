def appendAndDelete(s, t, k):
    # print('array s', s[6:])
    # print('array t', t[6:])
    
    # create a variable that will hold where the descrepency begins 
    # create a for loop that will loop through both of the strings 
        # if at current index current letter in s is different than current
        # letter of t or len(s) - 1 is equal to index or len(t) - 1 is equal to 
        # index
            # return descrepency index 
        
    divergence = None 
    
    for index in range(len(s)):
        if len(s) - 1 == index and len(t) - 1 != index:
            divergence = index + 1
            break
        elif len(s) - 1 != index and len(t) - 1 == index:
            divergence = index + 1
            break
        elif len(s) - 1 == index and len(t) - 1 == index:
            divergence = -1
            break
        elif s[index] is not t[index]:
            divergence = index 
            break 
        
    if divergence == -1:
        return 'Yes'
    else:
        print('divergence value', divergence)
                
        diffS = len(s[divergence:])
        diffT = len(t[divergence:])
        print('sum of divergence', diffS + diffT)
        
        if diffS + diffT > k and (diffS + diffT) % 2 != k % 2:
            return 'No'
        else:
            return 'Yes'