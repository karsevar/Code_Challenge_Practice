# first solution: time complexity is a little below O(n^2) but not by much.
# Will need to use a hash table to decrease the time complexity down to 
# O(n * log(n)) or O(n) if possible.

def pairs(k, arr):
    print('target value', k) 
    print('input array', arr)
    
    # create a counter variable that will keep track of all the 
    # times the target value is created 
    
    # create a for loop that will loop through the array discounting 
    # the last index 
        # create an inner loop that will start at the index of the outer loop 
        # and end at the last index of the array (it seems that I don't have to 
        # worry about recurring values)
            # if the difference between the outer loop index and the inner loop index is 
            # equal to k 
                # iterate the counter by one 
    
    target_counter = 0 
    
    for outer_index in range(len(arr) - 1):
        for inner_index in range(outer_index, len(arr)):
            if abs(arr[outer_index] - arr[inner_index]) == k:
                target_counter += 1
                
    return target_counter