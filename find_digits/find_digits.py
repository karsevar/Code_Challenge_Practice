def findDigits(n):
    # youtube tutorial solution using absolute divisor symbol // 
    # the mudelo symbol % 

    # as a means to not modify the passed in n variable
    
    # create a while loop that will terminate once n is less than zero 
        # create a remainder variable that will take on the value 
        # n % 10 (the final digit of n).

        # create an if statement that will be used to ignore remainder values 
        # that are zero and num % remainder values that are equal to zero 
            # increment the counter 

        # increment n by one digit place through n // 10 

    num = n
    counter = 0 

    while n > 0:
        r = n % 10 
        print('remainder', r)

        if r != 0 and num % r == 0:
            counter += 1

        n = n // 10 

    return counter