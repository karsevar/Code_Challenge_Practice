def pickingNumbers(a):
    # Write your code here

    # explored set() variable that keeps track of the explored values 
    # since we are only looking for combinations and not permutations.

    # largest_length variable

    # create a for loop that will increment through each value in a
        # create a positive length that counts any value that is one integar greater 
        # than the current value 
        
        # create a negative length that counts any value that is one integer less than
        # the current value 
        # if the current value is not in explored 
            # run another for loop through the rest of the list starting at 
            # the current value
            
            # if j_value is equal to current_value + 1:
                # increment positive length by one 
                # add j_value to explored
            # if j_value is equal to current_value - 1:
                # increment negative length by one 
                # add j_value to explored

        # if largest_length is less than positive length or negative length 
            # over write largest_length 

    explored = set() 

    largest_length = 0 

    for current_index in range(len(a)):

        positive_length = 0 
        negative_length = 0

        if a[current_index] not in explored:
            for compare_index in range(current_index, len(a)):
                explored.add(a[current_index])
                if a[compare_index] == a[current_index] + 1:
                    positive_length += 1 
                    explored.add(a[compare_index])
                elif a[compare_index] == a[current_index] - 1:
                    negative_length += 1 
                    explored.add(a[compare_index])
                elif a[compare_index] == a[current_index]:
                    negative_length += 1 
                    positive_length += 1

        if positive_length > negative_length:
            if largest_length < positive_length:
                largest_length = positive_length 

        elif negative_length >= positive_length:
            if largest_length < negative_length:
                largest_length = negative_length

    return largest_length