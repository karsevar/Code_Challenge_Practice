# unoptimized solution to this problem.
def countTriplets(arr, r):
    print('array', arr)
    
    # the initial idea is to use the combinations logic to find the possible 
    # triplets that fit the specifications of the problem.
    
    # the problems this method creates is that I will need to create a separate 
    # hash table that will carry all of the recuring values in the array and iterate 
    # through the count upon using each recurring value.
    
    # create a hash table that will carry all the values in the array with their 
    # corresponding count in the array 
    # create a new array that will only house the values that are a multiple of r 
    
    # create a for loop that will iterate through the arr 
        # if the value is not in hash table add it to the hashtable 
        # if no iterate the count by one 
        
    values_map = {}
    new_array = []
    count = 0
    
    for number in arr:
        if number not in values_map:
            values_map[number] = 1
        else:
            values_map[number] += 1
        
        if number % r == 0 or number == 1:
            new_array.append(number)
            
    # print('values_map', values_map)
    # print('new_array', new_array)
    visited = set()
    
    for i in range(len(new_array)-2):
        for j in range(i+1, len(new_array)-1):
            for k in range(j+1, len(new_array)):
                if new_array[i]*r == new_array[j] and new_array[j]*r == new_array[k] and (new_array[i], new_array[j], new_array[k]) not in visited:
                    # print('permutation', new_array[i], new_array[j], new_array[k])
                    visited.add((i, j, k))
                    count += 1
                    
    return count

# Still not passing all test cases but now the code should be more optimized.
def countRefactorTriplets(arr, r):
    # create a map that will carry an array of arrays that carry sequential values 
    
    # iterate through the array:
        # check if the value is in the map 
            # if not add the value times r as the key and the value as the value 
            # if yes get the values from the key 
                # check if the values are length 2 
                    # if yes iterate counter by one 
                    # if not create a new key with the value times r and 
                    # add the arrays with the new value appended to the bottom of
                    # each array.
                    
    counter = 0 
    value_map = {}
    
    for value in arr:
        if value not in value_map:
            value_map[value * r] = [[value]]
        else:
            for array in range(len(value_map[value])):
                if len(value_map[array]) == 2:
                    counter += 1
                    value_map.pop(array)
                    
            if (value * r) not in value_map:
                value_map[value * r] = [[value]]
                for value_array in value_map[value]:
                    value_map[value * r].append(value_array[:] + [value])
            else:
                value_map[value * r].append([value])
                for value_array in value_map[value]:
                    value_map[value * r].append(value_array[:] + [value])   
                    
    return counter