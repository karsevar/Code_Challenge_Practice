def catAndMouse(x, y, z):
    # keep in mind that x and y are the cats and z is the mouse.
    
    # this solution doesn't require a loop only arithematic the only problem is 
    # coding a solution where either catA or catB will be a number of indices 
    # ahead of the mouse and still be able to compare the one cat values 
    
    # first find the difference between catA and the mouse
    # find the difference between catB and the mouse
    
    # if the difference for catA is greater than catB
        # return catB 
    # if the difference for catB is greater than catA
        # return catA 
    # if the values of catA and catB are the same return mouse 

    catA = abs(z - x)
    catB = abs(z - y)
    
    # print('catB and catA', catA, catB)
    
    if catA > catB:
        return 'Cat B'
    elif catA < catB:
        return 'Cat A'
    else:
        return 'Mouse C'