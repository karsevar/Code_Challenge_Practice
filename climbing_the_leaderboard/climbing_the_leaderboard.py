def climbingLeaderboard(scores, alice):

    # create a new array that deletes all the repeating scores 
    new_scores = []
    for index in range(1, len(scores)):
        if len(new_scores) == 0:
            new_scores.append(scores[index-1])
        if scores[index-1] > scores[index]:
            new_scores.append(scores[index])
    # create another O(n) operation where I will loop through the 
    # scores array again with each value in the alice array and find 
    # the respective ranking of each alice score value 

    # create a for loop that will iterate over the alice array 

            # create another for loop that will iterate over the new_scores array
                # if the alice's scores is greater than or equal to the current index of 
                # new_score print the index position 
    rankings = []

    for alice_score in alice:
        for score_index in range(len(new_scores)):
            if alice_score >= new_scores[score_index]:
                rankings.append(score_index + 1)
                break
            if score_index == len(new_scores) - 1:
                if new_scores[score_index] <= alice_score:
                    rankings.append(score_index + 1)
                else:
                    rankings.append(score_index + 2)
    return rankings
