def angryProfessor(k, a):

    print('threshold', k)
    print('array', a)
    
    # naive solution is to loop through the a (array) and 
    # have a counter increment whenever a specific index in a
    # is more than one 

    attendence = 0 

    for student in a:
        if student <= 0:
            attendence += 1 

    if attendence >= k:
        return 'NO'
    else:
        return 'YES'