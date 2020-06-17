def arrayManipulation(n, queries):
    # create the array with the n argument 
    # each place in the array will be initialized to zero 
    # create a largest_value variable that will be initialized to zero 

    # create a for loop that will loop through each query in queries 
        # create a for loop that will loop through the index positions as 
        # instructed by query[0] (start) and query[1] (end) make sure to 
        # minus one from the start index as the start is zero indexed 
            # in each index position add query[2] 

            # if query[2] and the value in the current index position is 
            # greater than largest_value 
                # overwrite largest_value with query[2] plus value in current index
                # position 

    array = [0] * n 
    largest_value = 0 

    for query in queries:
        for index in range(query[0] - 1, query[1]):
            array[index] += query[2]

            if array[index] > largest_value:
                largest_value = array[index]

    print(array)

    return largest_value


# optimized solution using the example from:
# https://www.youtube.com/watch?v=JtJKn_c9lB4

def arrayManipulationRefactor(n, queries):

    array = [0] * (n) 
    largest_value = 0 

    for query in queries:
        
        array[query[0]-1] += query[2]
        if query[1] != len(array):
            array[query[1]] -= query[2]

    for index in range(1, len(array)):
        array[index] += array[index-1]

        if largest_value < array[index]:
            largest_value = array[index]

    print(array)
    return largest_value