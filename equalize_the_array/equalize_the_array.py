def equalizeArray(arr):

    # create a hashmap that is initialized as empty
    # keep a variable that will remember the key with the highest frequency
    # initialize it to arr[0]
    # create a loop that will populate the hashmap with the value frequencies 
    # in arr.
        # hashmap[current_value] += 1 
        # check if hashmap[current_value] > variable with highest frequency
        
    # return len(arr) - highest_frequency_value 

    frequencies = {}
    highest_frequency = arr[0] 

    for current_value in arr:
        if current_value not in frequencies:
            frequencies[current_value] = 1 
        else:
            frequencies[current_value] += 1

        if frequencies[current_value] > frequencies[highest_frequency]:
            highest_frequency = current_value 

    print('frequencies hashmap', frequencies)
    print('highest frequency value', highest_frequency)

    return len(arr) - frequencies[highest_frequency]