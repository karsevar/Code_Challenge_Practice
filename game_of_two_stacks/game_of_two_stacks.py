def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    
    # first iterate through the a stack and try to populate another 
    # array called elements with the values that add up to or below the x 
    # value
    
    # create a topA variable initialized to zero 
    # create an elements array 
    # create a sum variable 

    # create a while loop that will terminate once sum is equal to or 
    # more than x or if topA is at the end of the array

    topA = 0 
    elements = []
    sumx = 0 
    a_count = 0

    while True:
        if topA == len(a):
            break
        elif sumx + a[topA] > x:
            break
        elif sumx + a[topA] <= x:
            elements.append(a[topA])
            sumx += a[topA]
            topA += 1
            a_count += 1

    # print(elements)
    # print(x)
    print('stack a', a) 
    print('stack b', b)
    print('x variable', x)
    topB = 0
    b_count = 0
    
    maxIndex = a_count 

    while topB < len(b):
        sumx += b[topB]
        topB += 1
        b_count += 1 
        while sumx > x and len(elements) > 0:
            lastValue = elements.pop()
            a_count -= 1
            sumx -= lastValue 

        if sumx <= x and b_count + a_count > maxIndex:
            maxIndex = b_count + a_count 

    return maxIndex