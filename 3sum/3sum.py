class Solution:
    def threeSum(self, nums):
        # according to the hints make sure to keep the first value in the 
        # array the same and iterate through the rest of the array much like 
        # finding 2sum problem.
        
        # edge case for an empty array
        
        # edge case for an array that is less than 3 in length 
        
        # edge case if the array is more than or equal to 3 in length 
            # initialize a solution array in which the triplets will be appended 
            # into 
            
            # create a dictionary that will hold all the double values 
            
            # a create a for loop that will start at index 1 and end one value before 
            # the last value in array
                # create another for loop that will loop from one index after the 
                # current index in the outer loop
                    # fill up the dictionary with the sum of the two values make sure
                    # to account for duplicates
                    
                    
        if len(nums) < 3:
            return []
        else:
            solutions = []
            nums.sort()
            
            for x_index in range(len(nums)):
                if x_index != 0 and nums[x_index] == nums[x_index-1]:
                    continue    
                else:
                    y_index = x_index +1
                    z_index = len(nums) - 1
                    
                    while y_index < z_index:
                        current_sum = nums[x_index] + nums[y_index] + nums[z_index]
                        
                        if current_sum == 0:
                            solutions.append([nums[x_index], nums[y_index], nums[z_index]])
                            y_index += 1
                            while nums[y_index] == nums[y_index - 1] and y_index < z_index:
                                y_index += 1
                                
                        elif current_sum > 0:
                            z_index -= 1
                        elif current_sum < 0:
                            y_index += 1
                        
            return solutions