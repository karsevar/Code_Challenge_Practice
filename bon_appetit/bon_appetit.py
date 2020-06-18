def bonAppetit(bill, k, b):

    # first calculate the sum of the bill discounting k element 

    # if the sum is equal to the b argument:
        # print Bon Appetit

    # else
        # minus the b argument by the sum element and return the difference 

    # print(bill)
    # print(k)
    # print(b)

    discard_value = bill.pop(k)
    actual_split = sum(bill) // 2
    # print('actual split', actual_split)

    if actual_split == b:
        print('Bon Appetit')
    else:
        print(b - actual_split)