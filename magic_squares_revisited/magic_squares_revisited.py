def magicSquares(n=3):

    # first create a magic square approximation with python arrays (make sure that 
    # the number of rows are columns in the 2D matrix are equal to n)

    # find the sum constant for the n by n dimenstions of the magic square

    # place the initial 1 value in the (n/2, n - 1) index position of the magicArray 

    # set the initial position for the index variables row: n/2 col: n - 1

    # create a for loop that will go from 2 to n^2 
        # if row is equal to -1 and col is equal to n:
            # increment the row and col to 0 and n - 2 respectively 

        # elif row is equal to -1:
            # increment the row index to n - 1
        
        # elif col is equal to n:
            # increment the col index to 0 

        # else
            # increment both row and col by row -= 1 and col += 1 

        # place current value in row and col position of the magicArray

    # return the magicArray variable

    magicSum = (n * ((n ** 2) + 1)) / 2

    magicArray = []

    for _ in range(n):
        magicArray.append([0]*n)

    row = n // 2 
    col = n - 1 

    magicArray[row][col] = 1

    for num in range(2, (n**2) + 1):
        row -= 1 
        col += 1

        if row == -1 and col == n:
            row = 0 
            col = n - 2

        if row == -1:
            row = n - 1

        if col == n:
            col = 0 

        if magicArray[row][col] != 0:
            row += 1 
            col -= 2


        # print('row', row)
        # print('col', col)
        # print('value', num) 
        # print('magicArray', magicArray)

        magicArray[row][col] = num

    
        

    return magicArray


print(magicSquares(7))