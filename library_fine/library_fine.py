def libraryFine(d1, m1, y1, d2, m2, y2):
    print('month', type(m1))
    print('day', d1)
    print('year', y1)

    # create a check to see if the book is returned on the same year 
    # if not:
        # return 10000 
    # if so 
        # check if the book is returned on the same month:
            # if not check if the month in which the book was returned 
            # is less then the due date:
                # if so return 0 
                # else:
                    # calculate the fine amount 

            # if so:
                # check if the return day is less than or equal to the due date 
                    # if so return 0 
                    # else calculate the fine amount 

    if y2 == y1:
        if m2 == m1:
            if d2 >= d1:
                return 0 
            else:
                return (d1 - d2) * 15 
        else:
            if m2 > m1:
                return 0 
            elif m2 < m1:
                return (m1 - m2) * 500 
    elif y2 > y1:
        return 0 
    elif y2 != y1:
        return 10000 