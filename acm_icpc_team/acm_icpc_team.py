def acmTeam(topic):
    print(topic)
    
    # create a variable that will carry the highest number of subjects 
    # a group has covered 

    # create a counter that will count the number of groups that display the 
    # highest number of subjects covered.

    # create a for loop that will loop through topic 
        # create another for loop that will start at one 
        # index after the outerloop's current index to len(topic) - 1 
        # (this will exclude the last index)
            # use bitwise or operation to find the number of subjects 
            # the current group covers 

            # create another loop that will loop through the binary result 
            # of the last operation and count the number of subjects covered.

            # check if the group's number of subjects covered is greater than 
            # the highest number of subjects variable 
                # if so overwrite highest number of subjects variable with the group's
                # subject count and restart group counter to one 
                
                # if the two values are equal iterate the group counter by one 

    highest_subject_count = 0 
    highest_group_count = 0 

    for first_student in range(len(topic) - 1):
        for second_student in range(first_student + 1, len(topic)):
            # print('first_student', topic[first_student])
            # print('second_student', topic[second_student])

            subjects_binary = int(topic[first_student], 2) | int(topic[second_student], 2)
            # print('group binary count', bin(subjects_binary))

            current_subjects_count = 0 
            for value in bin(subjects_binary):
                if value == '1':
                    current_subjects_count += 1

            if current_subjects_count > highest_subject_count:
                highest_subject_count = current_subjects_count 
                highest_group_count = 1
            elif current_subjects_count == highest_subject_count:
                highest_group_count += 1

    return [highest_subject_count, highest_group_count]