def permutationEquation(p):
    # create a hash table that contains the 1 indexed position of a variable as the key 
    # and the value as the value 
    value_hash = {}
    index = 0
    for value in p:
        index += 1 
        value_hash[value] = index 

    solution = []
    for x in range(1, len(p)+1):
        print(x)
        intermediate_value = value_hash[x]
        solution.append(value_hash[intermediate_value])

    return solution