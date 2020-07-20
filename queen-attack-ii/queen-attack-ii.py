def queensAttack(n, k, r_q, c_q, obstacles):
    print(n) 
    print(r_q, c_q)
    print('obstacles', obstacles)

    # first find the directions in which the queen piece can move in the 
    # up, down, left, right, and the four diagonal directions.

    # to find the number of squares the queen can move up without any
    # obsticles is subtract r_q by n (the dimensions of the board)

    # to find the number of squares the queen can move up without any
    # obsticles simply store the queen's r_q position in a variable and 
    # minus it by one 

    up_move = n - r_q 
    down_move = r_q - 1
    left_move = c_q - 1
    right_move = n - c_q 

    # find the diagonal moves the piece can make 
    # top left diagonal: 
    # store up_move if left_move value is left_move is smaller or the inverse
    # top right diagonal: 
    # store up_move if left_move value is right_move is smaller or the inverse
    # bottom left diagonal: 
    # store down_move if left_move value is left_move is smaller or the inverse
    # bottom right diagonal: 
    # store down_move if left_move value is right_move is smaller or the inverse

    up_left_move = up_move if up_move < left_move else left_move 
    up_right_move = up_move if up_move < right_move else right_move 
    down_left_move = down_move if down_move < left_move else left_move 
    down_right_move = down_move if down_move < right_move else right_move
    
    # now let's calculate the number of squares the queen piece can move 
    # with the introduction of obsticles.
    # create a for loop that will loop through all the obsticle coordinates in 
    # obsticles array 
        # up moves with obsticle: 
        # Check if q_r + (obsticle row - q_r) and q_c is equal to obsticle row and column
            # if so check if up_move is greater than obsticle 
                # if so over write up_move with obsticle row - q_r 

        # down moves with obstricle:
        # check if q_r - obsticle row and q_c is equal to obsticle 
            # if so check if down_move is greater than obsticle 
                # if so over write down_move with q_r - obsticle row 

    for obstacle in obstacles:
        print('obstacle', obstacle)
        print('obstacle in down movement', r_q - (r_q - obstacle[0]) == obstacle[0])

        if c_q == obstacle[1]:
            if r_q < obstacle[0]:
                up_move = (obstacle[0] - r_q) - 1
            else:
                down_move = (r_q - obstacle[0]) - 1
        elif r_q == obstacle[0]:
            if c_q < obstacle[1]:
                right_move = (obstacle[1] - c_q) - 1
            else:
                left_move = (c_q - obstacle[1]) - 1
                
    print('up', up_move, 'down', down_move, 'left', left_move, 'right', right_move)

    return up_move + down_move + right_move + left_move + up_left_move + up_right_move + down_left_move + down_right_move