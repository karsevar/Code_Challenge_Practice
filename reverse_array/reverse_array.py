def reverseArray(a):
    
    # first attempt use reverse indexed for loop to 
    # append the values in a in reverse order.

    # create a new array 

    # create a for loop that will start at the last index of the 
    # array and iterate down towards the first index 

    new_array = []

    for index in range(len(a)-1, -1, -1):
        new_array.append(a[index])

    return new_array