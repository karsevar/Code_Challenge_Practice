def howManyGames(p, d, m, s):
    # Return the number of games you can buy

    # create a variable that will serve as the game 
    # counter

    # The naive solution is to create a while loop that will
    # terminate once p is more than s 
        # check if p is not equal to m 
            # minus s by p 
            # minus p by d 
            # increment game counter by one 
        # else 
            # minus s by p 
            # increment game counter by one 

    game_counter = 0 

    while s >= 0:
        print('s', s, 'p', p)
        if p > m:
            s -= p 
            p -= d 
            game_counter += 1 

        elif p <= m:
            p = m
            s -= p 
            game_counter += 1 

    return game_counter - 1