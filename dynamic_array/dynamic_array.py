def dynamicArray(n, queries):
    # Write your code here
    
    # create a list within a list. Example:
    # seqList = [
    # sequence 0 
    # [],
    # sequence 1 
    # [],
    # sequence n - 1
    # ....
    # ]

    # print(queries)

    # initialize lastValue to 0 

    # since the queries are passed into the function as an array in an array 
    # create a for loop that will loop through all the subarrays in queries 
        # if the first value in the subarray is 1:
            # append value in subarray[2] into sequence subarray[1]

        # elif the first value in the subarray is 2:
            # overwrite lastValue by seqList[query[1]][query[2]]
            # print lastValue

    seqList = [[] for _ in range(n)]
    lastValue = 0
    results = [] 

    for query in queries:
        if query[0] == 1:
            seq_index = (query[1] ^ lastValue) % n
            seqList[seq_index].append(query[2])
            # print(seqList)
        elif query[0] == 2:
            seq_index = (query[1] ^ lastValue) % n
            index = query[2] % len(seqList[seq_index])
            lastValue = seqList[seq_index][index]
            results.append(lastValue)
            print(lastValue)

    return results