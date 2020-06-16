def matchingStrings(strings, queries):
    # convert the elements in queries from only 
    # being in an array into a hashtable
    # example of query hashtable 
    # {
    #   'abd': 0,
    #   'adb': 0,
    #   ....
    # }

    # loop through the strings array and find if the current string 
    # is in the queries dictionary 
        # if so iterate the key's value by one 

    # loop through the queries dictionary and place all the values into 
    # a new array 
    # return the array 

    query_dict = {}
    for query in queries:
        query_dict[query] = 0

    print(queries)
    print(len(query_dict) == len(queries))

    for string in strings:
        if string in query_dict:
            query_dict[string] += 1
    
    return [query_dict[key] for key in queries]