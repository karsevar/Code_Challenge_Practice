def cavityMap(grid):
    print(grid[0][0])
    
    # might need to create a new array since one can't modify 
    # a string without the splice method.
    
    # create a for loop that will iterate through the x axis 
    # specifically the rows of the matrix make sure that the 
    # for loop starts at row index 1 and ends at n - 2
    
        # create an additional for loop that will iterate through the X 
        # axis make sure that the loop begins at column index 1 and ends 
        # at column index n - 2 
            
            # check if the neighbors (top, down, right, left) are all 
            # smaller than the current cell 
            # if so change the current cell value to X 
    
    if len(grid) == 2 and len(grid[0]) == 2 or len(grid) == 1 and len(grid[0]) == 1:
        return grid
    else:
        new_grid = []
        new_grid.append(grid[0])
        
        for row in range(1, len(grid) - 1):
            columns = list(grid[row])
            # print('columns', columns)
            for column in range(1, len(grid[row]) - 1):
                # print('column', columns[column])
                if grid[row][column] > grid[row+1][column] and grid[row][column] > grid[row-1][column] and grid[row][column] > grid[row][column-1] and grid[row][column] > grid[row][column+1]:
                    columns[column] = 'X'
                    
            new_grid.append(''.join(columns))
            
        new_grid.append(grid[-1])
            
        return new_grid