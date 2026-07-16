class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sliding window solution first try.
        current_sum = sum(nums[:k])
        maximum_average = current_sum/k
        cache = {}

        for i in range(len(nums) - k):
            current_sum = (current_sum - nums[i]) + nums[i+k]
            current_average = current_sum/k
            

            if current_average > maximum_average:
                maximum_average = current_average

        return maximum_average
    
# I believe that the time complexity can be O(n) since in the worst case k can be set to 1 which means 
# that we will have to loop through the entire array. Calculations have a minimal computational cost since 
# We are only subtracting and adding one element at a time and we are only calculating the mean at the end of the function.
class SolutionSlidingWindowRevisit:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # I can understand how this can be considered a fixed window problem as you are forced to calculate the maximum average of a subarray of size k in a specific squence. 

        # okay so we don't have to worry about k being greater than nums according to the constraints. 

        # to start the for loop I think all I need to do is calculate the starting sum from 0:k within the nums array and in addition the largest sum should be the largest average due to how the mean is always scewed due to outliers in the dataset.

        # create the initial sum of nums array through sum(nums[0:k+1])

        # create a for loop that will start at k and end at len(nums) - 1
        # for each iteration of the loop subtrace the current index from the running current_sum value and add the next index value to the current_sum value.

        # check if current sum is greater than maximum_sum if true replace maximum_sum with current_sum 

        # return maximum_sum/k

        current_sum = sum(nums[:k])

        maximum_sum = current_sum

        end_index = 0

        for i in range(k, len(nums)):
            current_sum -= nums[end_index]
            current_sum += nums[i]

            if current_sum > maximum_sum:
                maximum_sum = current_sum
            end_index += 1

        return maximum_sum/k