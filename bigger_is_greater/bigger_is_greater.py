def biggerIsGreater(w):
    # first convert the string into an array for easier lookup and 
    # inplace manipulation.
    word_array = list(w)
    
    # loop through the word_array from the last value to the 
    # first value terminate the loop once the current index is 0 
        # if the next character is greater than the current character 
            # keep the index position of the next character from the 
            # current character (call the variable pivot position).

    # second loop 
    # loop through the array starting at the pivot position find 
    # the value that is itermediately greater than the pivot position 
        # store the value as minimum_greatest 

    # swap the pivot position and minimum_greatest values within the 
    # array 

    # from the pivot position sort the array 
    pivot_character = None
    for character in range(len(word_array)-1, 0, -1):
        if word_array[character] > word_array[character-1]:
            pivot_character = character - 1
            break

    if pivot_character == None:
        return 'no answer'

    # print('pivot character in string', word_array[pivot_character])
    
    minimum_greatest = pivot_character + 1 
    for character in range(pivot_character+1, len(word_array)):
        # print('character index', character)
        if word_array[character] > word_array[pivot_character]:
            if word_array[minimum_greatest] > word_array[character]:
                minimum_greatest = character 
            
    # print('minimum character in string', word_array[minimum_greatest])

    word_array[pivot_character], word_array[minimum_greatest] = word_array[minimum_greatest], word_array[pivot_character]

    # print('word array after swap', word_array)
    from_pivot = word_array[pivot_character+1:]
    from_pivot.sort()

    # print('sorting experiment', from_pivot)
    # print('array from beginning to pivot', word_array[:pivot_character+1] + from_pivot)
    result = ''.join(word_array[:pivot_character+1] + from_pivot)
    print('result string', result)

    if result == w:
        return 'no answer'
    else:
        return result