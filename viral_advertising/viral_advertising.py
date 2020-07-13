def viralAdvertising(n):
    # create a variable that will hold the cumulative likes
    # create a variable that will hold the number of people 
    # in each day iteration.

    # create a for loop that will use n as the basis of the 
    # number of iterations 
        # divide the number of people variable by half 
        # iterate the cumulative likes variable divided number 
        # overwrite the people variable with the divided number variable times 
        # 3 

    cumulative_likes = 0 
    people = 5 

    for _ in range(n):
        half_network = people // 2 
        cumulative_likes += half_network
        people = half_network * 3
        
    return cumulative_likes