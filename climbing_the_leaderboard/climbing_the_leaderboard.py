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

def climbingLeaderboardRevised(scores, alice):

    # create a new array that deletes all the repeating scores 
    new_scores = []
    for index in range(1, len(scores)):
        if len(new_scores) == 0:
            new_scores.append(scores[index-1])
        if scores[index-1] > scores[index]:
            new_scores.append(scores[index])

    rankings = []
    
    if len(scores) > 1:
        for alice_score in alice:
            rankings.append(binary_search(0, len(new_scores)-1, new_scores, alice_score) + 1)
    else:
        for alice_score in alice:
            if scores[0] > alice_score:
                rankings.append(2)
            elif scores[0] <= alice_score:
                rankings.append(1)

    return rankings

def binary_search(start, end, scores, alice_score):
    # print('alice score', alice_score)
    while end >= start:
        # print('start', start)
        # print('end', end)
        middle = (start + end) // 2 
        # print('middle', middle, 'middle value', scores[middle], '\n')

        if start == end:
            if scores[start] > alice_score:
                return start + 1
            else:
                return start

        if scores[middle] > alice_score:
            start = middle + 1 
        elif scores[middle] < alice_score:
            end = middle
        elif scores[middle] == alice_score:
            return middle
