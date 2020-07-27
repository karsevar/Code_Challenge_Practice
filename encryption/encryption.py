import math

def encryption(s):
    print(s)

    # It seems that the input already has the white spaces removed 
    # so no need to create a separate step for white space removal.

    # find the number of characters within the input string 
    # find the square root of the resulting number of characters value 
    # calculate the bottom and ceiling values 

    # create a grid variable that will carry the string in the rows and 
    # columns.

    # create an if statement where on the off chance that bottom * 
    # ceiling is equal to or more than string length
        # grid columns equal ceiling and rows equal floor 
    # else 
        # grid columns and floor equal ceiling value 

    string_length = len(s) 

    string_square = math.sqrt(string_length) 

    ceiling = math.ceil(string_square)
    floor = math.floor(string_square)

    print('string length', ceiling)
    print('square root', floor)

    value_grid = []

    if (floor * ceiling) >= string_length:
        for row in range(floor):
            value_grid.append([''] * ceiling)
    else:
        for row in range(ceiling):
            value_grid.append([''] * ceiling)

    # print('initial grid', value_grid)

    # populate the resulting grid with the characters in string 
    # create a variable that will hold the current index in the string.
    # create a for loop that will first loop over the rows 
        # create an additional for loop that will loop over 
        # the columns in the grid 
            # if current index is equal to length of string 
                # break out of the loop 
            # populate the grid with current character in current index 
            # example value_grid[row][col] = s[current_index]
            # iterate current_index by one 

    string_index = 0 

    for row in range(len(value_grid)):
        for col in range(len(value_grid[0])):
            if string_index == len(s):
                break 
            value_grid[row][col] = s[string_index]
            string_index += 1

    print('value_grid after population', value_grid)

    solution_string = ''

    # create another nested loop setup that will loop through 
    # the value_grid again 
    row = 0 
    for col in range(len(value_grid[0])):
        for row in range(len(value_grid)):
            solution_string += value_grid[row][col]
        solution_string += ' '

    return solution_string