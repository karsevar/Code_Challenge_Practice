def formingMagicSquare(s):
    # according to online sources there are only nine possible 
    # magic square permutations for a 3 by 3 matrix.

    # create an array that contains the nine different magic square 
    # permutations.

    # create a variable that will carry the lowest possible cost 

    # create nested for loops that will first loop through the nine possible 
    # permutations (one at a time) and analyze whether each value in s or the 
    # possible permutation are the same or will need to be altered.

    # create a for loop that will go through the nine possible permutations 
    # as permutation 
        # create a total_cost variable that will keep track of the cost of 
        # converting a specific value within the s[row][col].

        # create another for loop that will loop through the rows 
            # create another for loop that will loop through the cols 
                # total_cost += abs(s[row][col] - permutation[row][col])

        # if total_cost is less than lowest_possible_cost variable over 
        # write the lowest_possible_cost variable with total_cost 

    permutations = [[8,1,6],[3,5,7],[4,9,2]], [[6,1,8],[7,5,3],[2,9,4]], [[4,3,8],[9,5,1],[2,7,6]],[[2,7,6],[9,5,1],[4,3,8]], [[2,9,4],[7,5,3],[6,1,8]], [[4,9,2],[3,5,7],[8,1,6]], [[6,7,2],[1,5,9],[8,3,4]], [[8,3,4],[1,5,9],[6,7,2]]

    lowest_cost = float('inf')

    for permutation in permutations:
        total_cost = 0 

        for row in range(len(s)):
            for col in range(len(s[0])):
                cost_in_segment = s[row][col] - permutation[row][col]
                total_cost += abs(cost_in_segment)

        if lowest_cost > total_cost:
            lowest_cost = total_cost 

    return lowest_cost