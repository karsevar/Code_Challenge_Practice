def organizingContainers(container):
    print(container)

    # create an array that will carry the rows 
    # create an array that will carry the cols 

    # create a for loop that will iterate through the each row 
        # make sure to sum the total of all the values in the current 
        # row and append it the sum to the rows array 

        # create a col_sum variable initialize the value to zero
        # create an additional for loop that will iterate through each of the 
        # columns in the matrix 
            # add the current column value to col_sum 

        # append col_sum to the cols array 

    # create an additional for loop that will iterate through the 
    # rows and columns 
        # check if the rows and columns are equal to each other 

    rows = []
    columns = []

    col_index = 0 

    while col_index != len(container[0]):
        column_sum = 0
        for row in range(len(container)):
            # print('column value', container[row][col_index])
            column_sum += container[row][col_index]

        columns.append(column_sum)
        col_index += 1 

    for row in container:
        rows.append(sum(row))

    # print('rows array', rows)
    # print('columns array', columns)
    rows.sort()
    columns.sort()

    for list_compare in range(len(rows)):
        if rows[list_compare] != columns[list_compare]:
            return 'Impossible'

    return 'Possible'