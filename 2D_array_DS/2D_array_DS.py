def hourglassSum(arr):

    print(arr)

    # create a column pointer 
    # create an array that carries all the sums 

    # create a while loop that will terminate once column pointer plus three 
    # is more than len(arr) 
        # create a row pointer 
        # create a while loop that will terminate once row pointer plus three 
        # is more than len(arr)
            # sum the top of the hour glass arr[col][row:row+3] 
            # find the middle number of the hour glass arr[col+1][row+1]
            # find the numbers at the bottom of the hour glass arr[col+2][row:row+3]
            # append the total sum of the hour glass in the array 
            # iterate row by one 

        # iterate col by one 

    col = 0 
    highest = float('-inf')

    while col+3 <= len(arr):
        row = 0 

        while row+3 <= len(arr[0]):
            # print(arr[col][row:row+3])
            # print(arr[col+1][row+1])
            # print(arr[col+2][row:row+3])

            upper_sum = sum(arr[col][row:row+3])
            lower_sum = sum(arr[col+2][row:row+3])
            total = upper_sum + arr[col+1][row+1] + lower_sum
            print('total sum', total)

            if highest < total:
                highest = total

            row += 1

        col += 1

    return highest