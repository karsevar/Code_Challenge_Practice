
# solution passes all test cases except for one because of the time complexity problem
# with finding a specific frequency in the frequencies dictionary will need to create
# separate dictionary that carries only frequencies.

def freqQuery(queries):
    # print('queries', queries)
    # create a hashtable that will hold all the values as the key and the frequency 
    # of each value 
    
    # create a for loop that will loop through all the queries 
        # if query[0] equals 1
            # if so insert the value in query[1] into the hashtable and 
            # initialize the count to one 
        # if query[0] equals 2
            # if yes decrement the frequency count of the value by one or 
            # delete the key from the hashtable if the frequency is one 
        # if query[0] equals 3 
            # loop through the hash table and find the first value 
            # that has the specified frequency 
            
    frequencies = {}
    solutionArray = []
    
    for query in queries:
        if query[0] == 1:
            if query[1] not in frequencies:
                frequencies[query[1]] = 1
            else:
                frequencies[query[1]] += 1 
                
        elif query[0] == 2:
            if query[1] in frequencies:
                if frequencies[query[1]] == 1:
                    del frequencies[query[1]]
                else:
                    frequencies[query[1]] -= 1
                
        elif query[0] == 3:
            frequencyFound = False
            for key in frequencies:
                if frequencies[key] == query[1]:
                    frequencyFound = True
                    break
            if frequencyFound:
                solutionArray.append(1)
            else:
                solutionArray.append(0)
                
    return solutionArray

# Optimized solution to finding a specific frequency. 
def freqQueryOptimized(queries):
    # print('queries', queries)
    # create a hashtable that will hold all the values as the key and the frequency 
    # of each value 
    # create another hash table that will hold the frequencies as the key and the 
    # value as the value.
    
    # create a for loop that will loop through all the queries 
        # if query[0] equals 1
            # if so insert the value in query[1] into the hashtable and 
            # initialize the count to one 
        # if query[0] equals 2
            # if yes decrement the frequency count of the value by one or 
            # delete the key from the hashtable if the frequency is one 
        # if query[0] equals 3 
            # loop through the hash table and find the first value 
            # that has the specified frequency 
            
    frequencies = {}
    frequence_value = {}
    solutionArray = []
    
    for query in queries:
        # print('frequency values in loop', frequence_value)
        if query[0] == 1:
            if query[1] not in frequencies:
                frequencies[query[1]] = 1
                if 1 not in frequence_value:
                    frequence_value[1] = set()
                    frequence_value[1].add(query[1])
                else:
                    frequence_value[1].add(query[1])
            else:
                frequence_value[frequencies[query[1]]].remove(query[1])
                frequencies[query[1]] += 1 
                
                if frequencies[query[1]] not in frequence_value:
                    frequence_value[frequencies[query[1]]] = set()
                    frequence_value[frequencies[query[1]]].add(query[1])
                else:
                    frequence_value[frequencies[query[1]]].add(query[1])
                
        elif query[0] == 2:
            if query[1] in frequencies:
                if frequencies[query[1]] == 1:
                    del frequencies[query[1]]
                    frequence_value[1].remove(query[1])
                else:
                    frequence_value[frequencies[query[1]]].remove(query[1])
                    frequencies[query[1]] -= 1
                    frequence_value[frequencies[query[1]]].add(query[1])
                    
                
        elif query[0] == 3:
            if query[1] in frequence_value and len(frequence_value[query[1]]) > 0:
                solutionArray.append(1)
            else:
                solutionArray.append(0)
    # print('frequency values', frequence_value)
                
    return solutionArray