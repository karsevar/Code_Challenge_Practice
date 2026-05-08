# iterative three sum solution with a lot of help from the video: https://www.youtube.com/watch?v=jzZsG8n2R9A&t=544s
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
        
    def threeSumTwoPointer(self, nums: List[int]) -> List[List[int]]:
        # according to an editorial you can use the normal two pointer algorithm to solve this. I believe that perhaps for the two pointer solution to work we will have to sort the array. A novel solution might be to set the i index through just having an outer for loop and the inner nested loop will be simply a while loop that will calculate the sum of the j and k indexes. This will effectively keep the inner loop's time complexity to O(n^2)

        # first sort the input nums array

        # initialize an empty output solutions array

        # setup a conditional that will return the solutions array if the length of the nums array is less than 3 
        # create a for loop that will set the i index and terminate at len(nums) - 2
        # initialize left pointer variable to i + 1
        # initialize right pointer variable to end of the nums array

        # create a while loop that will terminate when left and right pointers collide
        # if i + j + k indexes equals zero append the solutions array with the three values in an array
        # if the sum is greater than zero move the right pointer down one
        # if the sum is less than zero move the left pointer up one


        nums.sort()
        print(nums)

        solutions = []

        if len(nums) <= 2:
            return solutions

        for i in range(len(nums) - 2):
            left_pointer = i + 1
            right_pointer = len(nums) - 1
            while True:
                if left_pointer == right_pointer:
                    break
                
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if current_sum == 0:
                    subsolution_array = [nums[i], nums[left_pointer], nums[right_pointer]]
                    if subsolution_array not in solutions:
                        solutions.append(subsolution_array)

                if current_sum < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        return solutions