# brute force method with a time complexity of almost O(n^2) will need to 
# think up a solution utilizing hashtables.
class Solution:
    def maxArea(self, height):
        
        # create a max area variable initialized to zero 
        
        # create a for loop that will begin at the start of the array and 
        # end at the value before the last value 
            # create an additional for loop that will start at the value after 
            # the outer index variable 
                # create a height value that is the current index minus the ending
                # index make sure to add one to each of the values to counter act 
                # zero indexing. 
                
                # create a variable that will carry the tower with the lowest point 
                
                # times the two values together and check if the resulting value 
                # is greater than max area variable if so overwrite
                
        max_area = 0 
        
        for start_index in range(len(height)-1):
            for end_index in range(start_index + 1, len(height)):
                height_value = (end_index + 1) - (start_index + 1) 
                if height[start_index] > height[end_index]:
                    lowest_point = height[end_index]
                else:
                    lowest_point = height[start_index]
                    
                if max_area < (lowest_point * height_value):
                    max_area = (lowest_point * height_value)
                    
        return max_area

# the following solution is only a simplified version of the brute force 
# solution above. time complexity in the worst case can be calculated at 
# o(n)
class SolutionRefactored:
    def maxArea(self, height):
        
        # the hint said to start with a container that takes up the entire array 
        # and decrease the width only if there is a tower that is taller then 
        # the smallest tower
        i = 0 
        j = len(height) - 1
        max_area = 0 
        
        while i < j:
            if height[i] > height[j]:
                lowest_point = height[j]
            else:
                lowest_point = height[i]
                
            current_area = lowest_point * (j - i)
            if current_area > max_area:
                max_area = current_area
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return max_area