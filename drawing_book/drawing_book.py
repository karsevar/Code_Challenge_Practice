def pageCount(n, p):
    #
    # Write your code here.
    #

    # find the minimum number of pages that the person needs to turn 
    # This means that I will need to create two loops one loop simulating the 
    # starting page from the back 

    # A second loop that will simulate that the initial page is the first page 
    # in the book.

    # starting from the front page:
    
    if n % 2 == 0: 
        front_count = 0 
        initial_page = 1 

        while True:
            if initial_page -1 == p or initial_page == p:
                break
            front_count += 1
            initial_page += 2 

        back_count = 0 
        initial_page = n

        while True:
            if initial_page == n:
                if initial_page == p:
                    break

                back_count += 1
                initial_page -= 1
            elif initial_page -1 == p or initial_page == p:
                break 
            else:
                back_count += 1 
                initial_page -= 2 

        if back_count < front_count:
            return back_count
        else:
            return front_count

    else:
        front_count = 0 
        initial_page = 1 

        while True:
            if initial_page -1 == p or initial_page == p:
                break
            front_count += 1
            initial_page += 2 

        back_count = 0 
        initial_page = n

        while True:
            if initial_page -1 == p or initial_page == p:
                break 
            back_count += 1 
            initial_page -= 2 

        if back_count < front_count:
            return back_count
        else:
            return front_count