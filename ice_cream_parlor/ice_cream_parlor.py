def whatFlavors(cost, money):
    # print('money', money) 
    # print('cost', cost)
    
    # first create a hash table that will house the difference the pooled money 
    # and the current index cost of the ice cream flavor.
    
    # create a flavors array.
    
    # create a for loop that will loop through the cost array 
        # if current_cost is not in hashtable 
            # minus the total pooled money by the current index cost 
        # if not 
            # append the current index flavor cost to the flavors array and the 
            # value within hash_table[current_flavor]
            # remember to add one to all the indexes 
            
    combinations = {}
    flavors = []
    
    for current_cost in range(len(cost)):
        if cost[current_cost] not in combinations:
            combinations[money - cost[current_cost]] = current_cost 
        else:
            print(combinations[cost[current_cost]] + 1, current_cost + 1)
            break
            # flavors.append(current_cost)
            # flavors.append(combinations[cost[current_cost]])
            
    # print(flavors)