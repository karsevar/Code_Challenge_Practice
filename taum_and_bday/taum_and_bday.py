def taumBday(b, w, bc, wc, z):
    # Write your code here

    # create a variable named black_cost 
    # create a variable named white_cost 
    # check if bc + z is less than wc:
        # if so overwrite white_cost with b * (bc + z) 
        # overwrite black_cost with b * (bc) 
    # elif wc + z is less than bc:
        # if so overwrite black_cost with w * (wc + z) 
        # overwrite white_cost with w * (wc) 
    # else
        # overwrite black_cost with b * (bc + z) 
        # overwrite white_cost with w * (wc + z) 

    black_cost = 0 
    white_cost = 0 

    if (bc + z) < wc:
        white_cost = w * (bc + z) 
        black_cost = b * bc 
    elif (wc + z) < bc:
        white_cost = w * wc 
        black_cost = b * (wc + z)
    else:
        white_cost = w * wc 
        black_cost = b * bc 

    return white_cost + black_cost 