def hurdleRace(k, height):
    # create a largest_height variable that will carry the largest height in 
    # the array
    
    # loop through the height array 
        # update the largest_height variable if the current height is greater than
        # the largest_height 
        
    # if the largest_height is less than k 
        # return 0 
    # else 
        # return largest_height - k 
    
    largest_height = 0 
    
    for current_height in height:
        if largest_height < current_height:
            largest_height = current_height 
            
    if largest_height <= k:
        return 0 
    else:
        return largest_height - k