
def search(nums, target):
    print('list', nums)
        # we're trying to find the [4,5,6,2,3]
        
        # create a loop that will go through the array and find the 
        # pivot number (number in which the preceding and succeeding number is 
        # greater than the pivot)
    target_index = -1
        
    if nums[0] == target:
        return 0
        
    if len(nums) == 1:
        if nums[0] == target:
            return 0 
        else:
            return target_index
    else:
        for index in range(1, len(nums)):
            if target == nums[index]:
                target_index = index 

            if nums[index] < nums[index - 1]:
                if target > nums[index-1]:
                    break
                       
    return target_index