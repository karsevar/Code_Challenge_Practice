def beautifulDays(i, j, k):
    # create a beautiful day counter variable
    # first create a loop that will start at ith day and end at jth day plus one 
        # for each current day create a reversed integer and find the difference 
        # between the reversed day and the current day 

        # if the difference is divisible by k increment the beatiful day 
        # counter by one 

    beautiful_counter = 0 

    for current_day in range(i, j+1):
        reversed_int = ''
        day_string = str(current_day)
        for integer in range(len(day_string)-1, -1, -1):
            reversed_int += day_string[integer]

        if (current_day - int(reversed_int)) % k == 0:
            beautiful_counter += 1

    return beautiful_counter