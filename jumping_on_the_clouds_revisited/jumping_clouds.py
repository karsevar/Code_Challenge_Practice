def jumpingOnClouds(c, k):
    print('clouds', c)
    print('steps', k)

    # declare an index variable that will increment by the passed in 
    # argument k.

    # declare an energy variable initialized at 100 

    # increment index by one step 

    # create a while loop that will terminate once index equals zero 

    energy = 100
    index = (0 + k) % len(c) 

    if c[index] == 0:
        energy -= 1 
    elif c[index] == 1:
        energy -= 3 

    while index != 0:
        index = (index + k) % len(c)
        # print('index', index)
        if c[index] == 0:
            energy -= 1 
        elif c[index] == 1:
            energy -=3 

    return energy