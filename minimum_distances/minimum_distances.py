def minimumDistances(a):
    print(a)
    # the naive solution is to create a nested loop 
    # where the outer loop will begin at the start of the 
    # array and the inner loop will begin at the next index 
    # of the outer loop index.

    # main question is that are most of the arrays are 
    # palindromes?

    # create a minimum distance variable that will be 
    # initialized to zero 

    # create a for loop that will begin at the start of the 
    # passed in array 
        # create another for loop that will begin one index 
        # next from the outer loop index
            # check if a[outer_index] is equal to a[inner_index]
                # if so 
                # check if minimum distance variable is more 
                # then outer_index - inner_index or is equal to 
                # None 
                    # if so overwrite minimum distance variable 

    minimum_distance = -1

    for outer_index in range(len(a) - 1):
        for inner_index in range(outer_index + 1, len(a)):
            if a[outer_index] == a[inner_index]:
                if minimum_distance == -1 or minimum_distance > (inner_index - outer_index):
                    minimum_distance = inner_index - outer_index
                    
    return minimum_distance