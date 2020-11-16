def extraLongFactorials(n):
    # create a recursion helper function 
        # within the helper function 
            # the base case is if n is 1 
                # return n 
            # recursive case 
                # return n * helperfunction(n - 1)
            
    def factorial_helper(n):
        if n == 1:
            return n 
        else:
            return n * factorial_helper(n - 1)
        
    print(factorial_helper(n))