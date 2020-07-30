def timeInWords(h, m):
    # edge cases to consider the tens and the 40s are all measured as ten past 5 for
    # 5:10 and ten to 6 for 5:50 
    # create a hashtable that will carry integer to word conversions from ones to
    # twenties

    # create a results string variable
    
    # create an if statement that checks if minutes is less than or equal to 
    # 30 
        # add the hour conversion word into the results string 
        # (example results += hashtable[h]
        # if m is not zero
            # hashtable[m] + ' minutes' + ' past ' + results
    
    # if the minutes is more than 30 
        # we will need to convert the minutes passed into the function 
        # 60 - m = to minutes to the next hour 6:31 29 to seven 
        # if the hour is 12 
            # add one to results string 
        # else 
            # 
    print('hours', h)
    print('minutes', m)

    time_hash = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'quarter',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        21: 'twenty one',
        22: 'twenty two',
        23: 'twenty three',
        24: 'twenty four',
        25: 'twenty five',
        26: 'twenty six',
        27: 'twenty seven',
        28: 'twenty eight',
        29: 'twenty nine',
        30: 'half'
    }

    results = ''

    if m <= 30:
        results += time_hash[h]
        
        if m == 0:
            results += " o' clock"
        elif m == 1:
            results = time_hash[m] + ' minute past ' + results
        elif m == 15:
            results = time_hash[m] + ' past ' + results
        elif m == 30:
            results = time_hash[m] + ' past ' + results
        else:
            results = time_hash[m] + ' minutes past ' + results
    else:
        if h == 12:
            results += time_hash[1]
        else:
            results += time_hash[h + 1]

        new_minutes = 60 - m

        if new_minutes == 15:
            results = time_hash[new_minutes] + ' to ' + results
        elif new_minutes == 1:
            results = time_hash[new_minutes] + ' minute to ' + results
        else:
            results = time_hash[new_minutes] + ' minutes to ' + results
    
    return results