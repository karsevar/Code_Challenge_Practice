def twoStrings(s1, s2):
    # since the solution is only asking for a boolean the easiest solution is to 
    # simply place all the letters in one of the strings into a hash map and 
    # check if the other string contains the letters in the hashmap 
    
    # create a dictionary that will contain the letters in string 1
    # iterate through the letters in string 1 and place each letter into a 
    # hash table 
    
    # iterate through the letters in string 2 
        # check if the letter is in the letters hashtable 
        # if not return NO
    
    print('string 1', s1)
    print('string 2', s2)
    
    letters = set() 
    
    for letter1 in s1:
        letters.add(letter1)
        
    
        
    for letter2 in s2:
        if letter2 in letters:
            return 'YES'
    
    return 'NO'