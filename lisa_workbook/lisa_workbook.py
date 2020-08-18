def workbook(n, k, arr):
    # create a page count variable that will carry the 
    # current page count after each chapter

    # create a for loop that will loop through the each chapter
    # problem limit 
        # divide the current problem limit value by k 
        # make sure to use modulo operator and standard 
        # division which discounts the remainder

    page_count = 1
    special_problems = 0 

    for chapter in arr:
        start_page = page_count
        end_page = start_page + ((chapter // k) - 1)
        if (chapter % k) != 0:
            end_page += 1

        # create a for loop that will terminate once current 
        # page is more than end_page 
            # create antoher for loop that will terminate if 
            # the current problem number is equal to the page 
            # number, the problem_count variable is equal to k 
            # or chapter 

        problem_count = 0

        while page_count <= end_page:
            loop_counter = 0 

            print('page_count', page_count)
            
            while True:
                print('problem_count', problem_count)
                problem_count += 1 
                loop_counter += 1

                if page_count == problem_count:
                    special_problems += 1
                
                if problem_count == chapter:
                    break 
                elif loop_counter == k:
                    break

            page_count += 1

    return special_problems