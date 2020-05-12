def plusMinus(arr):
    # Create a counter for negative values 
    # positive values and values equal to zero

    # create a loop that will loop through the 
    # array and increment a specific counter 
    # if it fullfills a specific criteria.
        # if number is less than zero
            # increment negative counter by 
            # one 
        # if number is more than zero 
            # increment positive counter by 
            # one 

        # if the number is equal to zero 
            # increment zero counter by one 

    negative_counter = 0 
    positive_counter = 0 
    zero_counter = 0 

    for number in arr:
        if number > 0:
            positive_counter += 1 
        elif number < 0:
            negative_counter += 1 
        else:
            zero_counter += 1 

    print(round(positive_counter / len(arr), 6))
    print(round(negative_counter / len(arr), 6))
    print(round(zero_counter / len(arr), 6))