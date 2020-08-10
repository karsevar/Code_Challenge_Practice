def beautifulTriplets(d, arr):
    # create a modified nested loop that processes the 
    # possible permutations of the input array. 

    # the idea is that if a specific list within the nested loop
    # has 3 entries it will be considered a beautiful set and 
    # the main logic that will tell the loop whether a value 
    # should be entered in the array variable according to if 
    # the difference of the permutation set is equal to d

    # create a variable to will record the number of beautiful 
    # sets in the array 

    # create a for loop that will start at beginning of the 
    # array 
        # add the outerloop value to an initialized array 
        # called difference_set 

        # create an inner loop that will start at one index 
        # after the current index of the outer loop 
            # create a check if the difference_set is at length 
            # 3 if so 
                # increment the counter by one 
                # break out of loop 
            # if not 
                # check if difference between the inner loop 
                # variable is less then the last value in the 
                # difference array 
                    # if so add value to the difference array 

    triplets = 0 

    for outer_index in range(len(arr)-1):
        difference_array = []
        difference_array.append(arr[outer_index])

        for inner_index in range(outer_index, len(arr)):
            
            if (arr[inner_index] - difference_array[-1]) == d:
                difference_array.append(arr[inner_index])

            if len(difference_array) == 3:
                triplets += 1 
                break 
            
    return triplets