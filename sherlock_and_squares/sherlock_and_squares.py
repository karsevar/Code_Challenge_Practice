import math

def squares(a, b):
    print(math.sqrt(a))
    print(math.sqrt(b))

    # calculate the squares of a and b and assign them into their own variables 

    # create an if statement that checks if the squares of a and b have the same 
    # ones place value.
        # if so check if either a or b are not floating point decimal values
            # if so return 1
            # else return 0 

    # else:
        # round a and b and return the difference between a and b 

    a_sqrt = math.sqrt(a)
    b_sqrt = math.sqrt(b) 

    print(float(math.floor(a_sqrt)))
    print(float(math.floor(b_sqrt)))

    if float(math.floor(a_sqrt)) == float(math.floor(b_sqrt)):
        if a_sqrt == float(math.floor(a_sqrt)) or b_sqrt == float(math.floor(b_sqrt)):
            return 1 
        else:
            return 0 

    else:
        a_rounded = math.floor(a_sqrt) 
        b_rounded = math.floor(b_sqrt) 
        if a_rounded == a_sqrt:
            return (b_rounded - a_rounded) + 1
        else: 
            return b_rounded - a_rounded