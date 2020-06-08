def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    
    # first find the length of each of the stacks 
    # second find the initial sum of each of the stacks

    len1 = len(h1) 
    len2 = len(h2) 
    len3 = len(h3) 
    sum1 = sum(h1) 
    sum2 = sum(h2) 
    sum3 = sum(h3)
    
    top1 = 0
    top2 = 0 
    top3 = 0

    # create a while loop that will continue until the sums are equal to each other 
    # between the stacks or stacks 1 through 3 pointers are equal to the length of 
    # their respective stacks 
        # if sum1 2,3 are all equal to each other 
            # return the sum
        # if not check if sum1 is more than sum3 or sum2
            # if so iterate top1 by one index place 
            # minus sum1 by the value in top1 
        # check if sum2 is more than sum1 and sum3 
            # if so iterate top2 and do the same instructions as h1
        # check if sum3 is more than sum2 and sum3 
            # do the same instructions as h1 and h2
            
    while True:
        if sum3 == sum2 and sum2 == sum1:
            return sum2 
        elif sum1 > sum2 or sum1 > sum3:
            sum1 -= h1[top1] 
            top1 += 1 
        elif sum2 > sum1 or sum2 > sum3:
            sum2 -= h2[top2] 
            top2 += 1 
        elif sum3 > sum1 or sum3 > sum2:
            sum3 -= h3[top3] 
            top3 += 1