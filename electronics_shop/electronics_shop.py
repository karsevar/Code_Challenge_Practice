def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    print('keyboard prices', keyboards)
    print('drive prices', drives)
    print('money amount', b)
    
    # create a variable that will hold the current largest price of a keyboard and 
    # a usb drive.
    
    # create a for loop that will loop throughg the keyboards array 
        # create a for loop that will loop through the drives array 
            # add the keyboard and drive pair together 
            # check if the pair is more than the current largest price and less than the amount of money the user has 
                # if yes overwrite the current largest price with the current pair 
                
    # if current largest price is zero return -1 
    # if not return current largest price

    current_largest = 0 
    
    for keyboard in keyboards:
        for drive in drives:
            current_pair = drive + keyboard 
            
            if current_pair > current_largest and current_pair <= b:
                current_largest = current_pair 
                
    if current_largest == 0:
        return -1
    else:
        return current_largest