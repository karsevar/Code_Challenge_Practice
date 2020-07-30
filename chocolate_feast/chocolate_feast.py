def chocolateFeast(n, c, m):

    print('money', n)
    print('cost per bar', c) 
    print('wrapper exchange rate', m)

    # first calculate the number of chocolates you can buy with the 
    # initial amount of n (example n // c)
    # add the amount to the results variable 
    # This will give us the initial number of wrappers create the remaining_wrappers 
    # variable with the resulting value

    # create a while loop that will terminate wrappers remaining is less than
    # the wrapper exchange rate m 
        # calculate the number of chocolate bars you can buy with the number of 
        # remaining_wrappers (example remaining_wrappers // m)
        # update the remaining_wrappers variable with the modulo operator 
        # (example remaining_wrappers % m)
        # add the newly bought chocolate bars to the results variable 
        # add the newly bought chocolate bars wrappers to the remaining_wrappers 

    print('initial wrapper count', n // c)
    results = n // c 
    remaining_wrappers = n // c 

    while remaining_wrappers >= m:
        newly_bought_bars = remaining_wrappers // m 
        remaining_wrappers = remaining_wrappers % m 
        remaining_wrappers += newly_bought_bars 
        results += newly_bought_bars 

    return results
