class Solution:
    # this solution only was able to pass 18 out of the 21 test cases. 
    # it seems that they are looking for a solution where the original array is intact since we are only looking for a subarray that adds up to the target value. 
    # Time complexity is O(n) since we are only going through the array once in a single for loop
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        # smartest beginning move would be to simply sort the input array from least to greatest.
        # easiest first thought is to simply get the sum of all the values at the beginning. And use a for loop in such a way where I simply subtract each individual value from the overall sum until I reach the end of the array. 
        # I will need to record both the lenght of the subarray that creates the overall sum and the sum value.
        nums = sorted(nums)
        print("nums: ", nums)

        sum_value = sum(nums)
        subarray_length = len(nums)
        solution_length = subarray_length

        if sum_value < target:
            return 0

        for value in nums:
            sum_value -= value
            subarray_length -= 1  
            print("sum_value: ", sum_value, " subarray_length: ", subarray_length, "\n") 

            if sum_value >= target:
                solution_length = subarray_length  

        return solution_length     

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
        