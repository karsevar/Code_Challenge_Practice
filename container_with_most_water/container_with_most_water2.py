class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Okay so for this case the area calculation is simply the highest point times the number of containers between two distinct points. Since the indexes in an array are zero indexed we might need to add back one in order to create the appropriate calculations. 

        # first let's create the bruteforce solution

        # initialize the maximum area variable that will be set to zero

        # create a for loop that will keep track of the i index and will end on the second to last index
        # create a for loop that will keep track of the j index and that starts at i + 1 and ends at the end of the height array.
        # calculate the current area for the i and j index through finding which index point is the lowest and multiply that point by (j - i) + 1 (the number of containers between the two points)
        # if the calculated area is greater than the maximum recorded area overwrite the maximum area variable

        # return the maximum area variable

        # bruteforce method seems to have a time complexity of O(n^2) since in the worst case we are infact looping through the array twice.

        # maximum_area = 0

        # if len(height) <= 1:
        #     return maximum_area

        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         current_area = min(height[i], height[j]) * ((j - i)) 
        #         print("index i: ", i, " index j: ", j)
        #         print("height[i]: ", height[i], " height[j]: ", height[j])
        #         print("j - i + 1", (j - i) + 1)
        #         print("minimum height: ", min(height[i], height[j]))
        #         print("current sum: ", current_area, " \n ")
        #         if current_area > maximum_area:
        #             maximum_area = current_area

        # return maximum_area

        # two pointer solution
        # in order to make this solution work we will need to have conditionals that iterate either the left or right pointers. According to the editorials we will only iterate the smaller of the two points. calculating the current area will be carried out for each iteration of the overarching while loop.

        # initialize a left pointer that starts at beginning of the height array
        # initialize a right pointer that starts at the end of the height array

        # initialize the maximum area variable to zero

        # create a while loop that will terminate when left and right pointers collide
        # calculate the current area formula lowest point times right_pointer - left_pointer
        # if current area is greater than maximum_area overwrite maximum_area

        # if left pointer is less than right_pointer move left_pointer up one
        # if right pointer is less than left_pointer move right_pointer down one

        # return maximum_area

        # I believe that in the worst case this solution will have a time complexity of O(n) since we will only be iterating through the array at least one time using the right and left pointer.

        left_pointer = 0 
        right_pointer = len(height) - 1

        maximum_area = 0 

        if len(height) <= 1:
            return maximum_area

        while True:
            if left_pointer == right_pointer:
                break
            
            current_area = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
            if current_area > maximum_area:
                maximum_area = current_area

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return maximum_area