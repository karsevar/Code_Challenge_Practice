def designerPdfViewer(h, word):
    # print('letter heights', h)
    # print('word', word)
    
    # create an alphabet array 
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # loop through the alphabet array and create a new dictionary that will 
    # have the letters as the keys and letter heights as the values 
    
    alpha_dict = {}
    
    for index in range(len(alpha)):
        if alpha[index] not in alpha_dict:
            alpha_dict[alpha[index]] = h[index]
            
    # print('alpha dict', alpha_dict)
    
    # create a variable that will carry the letter with largest height
    
    # create another loop that will go through each letter in input word 
            # if current letter has greater height than largest_height 
            # over write largest height 
            
    # return largest_height * len(word)

    largest_height = 0 
    
    for letter in word:
        if largest_height < alpha_dict[letter]:
            largest_height = alpha_dict[letter]
            
    return largest_height * len(word)