# Complete the isValid function below.
def isValid(s):
    print('input string', s)
    
    # create a character dictionary that will house all the unique characters in 
    # the input string 
    
    # create a for loop that will loop through the input string 
        # if current index character is not in character dictionary 
            # create a new key with the character and initialize the value to one 
        # else iterate the value by one 
        
    # create a second loop that will iterate through the keys to find the minimum and 
    # maximum frequency of each character in the string and the number of strings that have maximum frenquency.
    
    # if maximum frienquency is one less than minmum and only one key has the maxiumum 
    # frequency return YES else NO

    char_dict = {}
    
    for character in s:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
            
    minimum_frequency = float('inf') 
    maximum_frequency = 0 
    maximum_count = 0 
    minimum_count = 0
    
    for key in char_dict:
        if minimum_frequency > char_dict[key]:
            minimum_frequency = char_dict[key]
            minimum_count = 1
        elif minimum_frequency == char_dict[key]:
            minimum_count += 1
            
        if maximum_frequency < char_dict[key]:
            maximum_frequency = char_dict[key]
            maximum_count = 1
        elif maximum_frequency == char_dict[key]:
            maximum_count += 1
    
    if maximum_frequency == minimum_frequency:
        return "YES"
    elif maximum_frequency - 1 == minimum_frequency and maximum_count == 1 or minimum_count == 1 and minimum_frequency == 1:
        return "YES"
    elif maximum_frequency - 1 == minimum_frequency and minimum_count == 1:
        return "YES"
    else:
        return "NO"