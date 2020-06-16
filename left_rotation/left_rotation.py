def left_rotate(arr, rotations):
    # initial solution:

    # Think that the entire array is a ring buffer where 
    # a value is taken from the back of an array and concatenated 
    # to the front.

    # create a loop that continues according to the passed in number of rotations
        # pop the last element in the array and place the popped element to the 
        # beginning
    
    for _ in range(rotations):
        lastValue = arr.pop(0)
        arr.append(lastValue)

    print(' '.join(map(str, arr)))