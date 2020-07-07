def utopianTree(n):
    # first create a meter counter initialized at 1 
    # initialize a cycle toggle that will toggle between 
    # sprint and summer. initial value will be spring

    # create a for loop that will continue until index >= n 
        # if cycle toggle is spring
            # double the meter counter 
            # change toggle to summer 

        # elif cycle toggle is summer 
            # add one meter to meter counter 
            # change toggle to spring 

    print(n)

    meter_counter = 1

    cycle_toggle = 'spring'

    for index in range(n):
        if cycle_toggle == 'spring':
            meter_counter *= 2 
            cycle_toggle = 'summer'
        elif cycle_toggle == 'summer':
            meter_counter += 1 
            cycle_toggle = 'spring'

    return meter_counter