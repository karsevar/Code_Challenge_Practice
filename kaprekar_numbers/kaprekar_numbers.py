def kaprekarNumbers(p, q):
    # create an array that will carry all the karparker numbers found in the 
    # range 
    
    # create a for loop that will go through the given range
        # create a new variable for the iteration number 
        # create another variable that will carry the number of original digits 
        # of the iteration number
        # square the iteration_variable 
        # convert the iteration_variable into a string 
        # split the iteration_variable into two halfs 
        # add the two halfs together and check if the sum equals the original 
        # iteration_variable value 
        # if so add to the array 
        
    nums = ''
    
    for original_num in range(p, q+1):
        iteration_variable = original_num ** 2
        number_digits = len(str(original_num))
        iteration_variable = str(iteration_variable)
        
        if len(iteration_variable) % 2 == 0:
            left_num, right_num = iteration_variable[:number_digits], iteration_variable[number_digits:]
        elif len(iteration_variable)% 2 != 0:
            left_num, right_num = iteration_variable[:number_digits -1], iteration_variable[number_digits-1:]
            if left_num == '':
                left_num = '0'
        
        num_sum = int(left_num) + int(right_num)
        
        if num_sum == original_num:
            nums += str(original_num) + ' '
    
    if len(nums) == 0:
        print('INVALID RANGE')
    else:
        print(nums)