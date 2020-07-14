def saveThePrisoner(n, m, s):
    print(n)
    print(m) 
    print(s)

    # the main idea is to increment s by one and start again 
    # to the first chair once the s variable is equal to n (
    # much like a ring buffer.

    # in addition make sure to increment m by one with each current 
    # chair position 

    # the naive solution is to create a while loop that will terminate 
    # once m is equal to zero (since m is the number of snacks to 
    # distribute).

    while m != 0:
        if m == 1:
            return s

        m -= 1 
        s += 1 

        if s > n:
            s = 1 