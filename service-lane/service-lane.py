def serviceLane(n, cases):
    print('cases', cases)
    print('service lane array', n)

    # create a results array

    # create a for loop that will iterate through cases 
        # initialize minimum width variable to positive infinity
        # create another for loop that will iterate through 
        # the input array from case[0] to case[1] + 1 
            # if current index width is less than minimum width 
            # variable
                # overwrite minimum width variable 

        # append minimum width variable to the results array 

    results = []

    for case in cases:
        minimum_variable = float('inf')

        for index in range(case[0], case[1] + 1):
            if minimum_variable > n[index]:
                minimum_variable = n[index]

        results.append(minimum_variable)

    return results