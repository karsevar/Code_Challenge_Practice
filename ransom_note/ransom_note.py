def checkMagazine(magazine, note):
    # print('magazine', magazine)
    # print('note', note)
    
    # create a set() that will contain the magazine words used for the note 
    
    # create a loop that will iterate through magazine array 
        # add the current word in magazine array to the set 
    
    # create a loop that will iterate through the note array 
        # check if current word in note array is in set 
            # if not return No
        
    words = {} 
    
    for word in magazine:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
        
    canCreateMessage = 'Yes'
        
    for word in note:
        if word not in words:
            canCreateMessage = 'No'
            break
        else:
            if words[word] == 0:
                canCreateMessage = 'No'
                break
            else:
                words[word] -= 1
        
    print(canCreateMessage)