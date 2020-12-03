# The following solution uses bubble sort which makes it a very unoptimal solution
# Will need to find a solution that has a O(n) time complexity
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # the easiest first solution is to use bubble sort to order the array 
        # in assending order.
        
        # create bubble boolean initialized to True 
        
        # create while loop that will continue to loop if True 
            # over write the bubble boolean to False 
            
            # create a for loop that will end before the last value in array 
                # check if the current index is greater than next index:
                    # if so swap the two values and overwrite the boolean to True 
                    
                    
        bubble_boolean = True 
        
        while bubble_boolean:
            bubble_boolean = False
            
            for current_index in range(len(nums)-1):
                if nums[current_index] > nums[current_index+1]:
                    nums[current_index+1], nums[current_index] = nums[current_index], nums[current_index+1]
                    bubble_boolean = True
                    
                    
        return nums