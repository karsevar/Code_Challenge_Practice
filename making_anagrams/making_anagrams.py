def makeAnagram(a, b):
    print('string a', a)
    print('string b', b)
    
    # create logic that will be used to discern which string is smaller a or b 
    
    # Create similar counter variable
    
    # use the larger of the two strings as the index character in the 
    # outer iteration loop
        # create inner loop with the smaller of the two strings 
            # if the two characters are the same iterate counter by two 
            
    # subtract counter by the total number of characters between both of the strings.
    
    # what happens if there are more than one of a similar character in a string 
    # I will need to create a loop where both strings can be modified in the loop 
    # so that duplicate characters won't be an issue
    
    # create a dictionary that will keep track of whether a character has been seen or 
    # not the key will be the character and the value will be the last index position
    
    char_dict = {}
    
    similar = 0
    
    if len(a) > len(b):
        smallest = b
        largest = a 
    else:
        smallest = a
        largest = b 
        
    for outer_character in range(len(largest)):
        for inner_character in range(len(smallest)):
            if largest[outer_character] == smallest[inner_character]:
                if smallest[inner_character] in char_dict:
                    if char_dict[smallest[inner_character]] != inner_character and char_dict[smallest[inner_character]] < inner_character:
                        similar += 2
                        char_dict[smallest[inner_character]] = inner_character
                        break
                else:
                    similar += 2 
                    char_dict[smallest[inner_character]] = inner_character
                    break
                    
    print('character dictionary', char_dict)
                
    return (len(a) + len(b)) - similar