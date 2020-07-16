def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        LHS = []
        RHS = []

        for element in arr[1:]:
            if pivot > element:
                LHS.append(element) 
            else: 
                RHS.append(element)

        LHS = quick_sort(LHS) 
        RHS = quick_sort(RHS)

        arr = RHS + [pivot] + LHS

    return arr

def cutTheSticks(arr):
    # using quick sort to sort through the passed in array in ascending order 
    # the smallest values will always be at the tail of the array 
    # new_arr = quick_sort(arr)
    new_arr = arr[:] 
    new_arr.sort(reverse=True)
    array_lengths = []
    
    # create a while loop that will terminate once new_arr length is zero:
        # print the length of the new_arr
        # pop the tail of the array 
        # create another while loop that will continue to pop off the array 
        # if the next value is equal to the minimum stick size.

        # create a for loop that will minus all the remaining sticks by the minimum 
        # stick size 

    while len(new_arr) > 0:
        array_lengths.append(len(new_arr))

        if len(new_arr) == 1:
            break

        minimum_stick = new_arr.pop() 
        print(new_arr)
        while len(new_arr) != 0 and new_arr[-1] == minimum_stick:
            new_arr.pop()

        for index in range(len(new_arr)):
            new_arr[index] -= minimum_stick 

    return array_lengths