def gridSearch(G, P):
    # print(G)
    # print(P)

    # use the same logic as hour glass sum.

    # create the search space that is the same columns and rows as 
    # the search pattern. Use the P dimensions to search within the 
    # G argument.

    # create a while loop that will terminate once row index is equal to 
    # len(G) + len(P) 
        # create a while loop that will terminate once column index is eqaul to 
        # len(G[0]) + len(p[0]) 
            # check if G[row][column:len(p[0])-1] is equal to P[0]
                # create a for loop that will loop from P[1] to P[len(P)-1]
                # to see if there is a matching pattern in the G 

            # iterate column by one 

        # iterate row by one 

    column_index = 0
    while (column_index + len(P)) <= len(G):
        row_index = 0 

        while (row_index + len(P)) <= len(G[0]):
            # print(G[column_index][row_index:row_index + len(P[0])])

            if P[0] == G[column_index][row_index:row_index + len(P[0])]:
                # print('match found in the first column')

                pattern_column = 0
                while pattern_column < len(P):
                    # print('pattern_column', pattern_column)
                    if column_index + pattern_column == len(G):
                        break
                    if G[column_index+pattern_column][row_index:row_index + len(P[0])] != P[pattern_column]:
                        break

                    if pattern_column == (len(P) -1) and G[column_index+pattern_column][row_index:row_index + len(P[0])] == P[pattern_column]:
                        return "YES"

                    pattern_column += 1

            row_index += 1
        column_index += 1
        
    return "NO"

# 4 6

# 123412

# 561212

# 123612

# 781234

# 2 2

# 12

# 34