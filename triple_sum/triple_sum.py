# This solution doesn't pass most of the test cases 
# will need to find a good resource to reason about this problem.
def triplets(a, b, c):
    print('a array', a)
    print('b array', b) 
    print('c array', c)
    
    # create an array that will carry all the values that reach the first constraint 
    # a value in array b that is equal to or greater than an element in array a 
    # can have duplicate values 
    
    # create a for loop that will loop through array a
        # create another loop that will loop through the elements of array b 
            # if the value in array a is equal to or less than the value in 
            # array b 
                # append the value to the array 
    
    # create a counter variable that will count the number of triplet pairs 
    
    # create a for loop that will loop through array c 
        # create another inner loop that will loop through the array from the first nested loop 
            # if the value in array c is less than or equal to value in output array 
                # iterate the counter 
                
    output_array = []
    
    for a_value in a:
        for b_value in b:
            if a_value <= b_value:
                output_array.append([a_value, b_value])
            
    triple_counter = 0
    visited = set()
    
    print('output array', output_array)
    
    for output_value in output_array:
        for c_value in c:
            if c_value <= output_value[-1] and (output_value[0], output_value[1], c_value) not in visited:
                triple_counter += 1
                visited.add((output_value[0], output_value[1], c_value))
                
    print('visited', visited)
                
    return triple_counter