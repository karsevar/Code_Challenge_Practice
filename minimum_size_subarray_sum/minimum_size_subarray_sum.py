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

class SolutionRevisit:
    # looking through this solution it seems that I'm only loop through the array once using two different pointers to find out the minimum substring sequence that a sum that equals or exceeds the target. 
    # time complexity can be interpreted as O(n) Uses the dynamic sliding window technique.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # So for this problem we can think in terms of the dynamic window algorithm where we can loop through the array and have a running target value that increases and decreases according to the elements placed in and removed out of it. 
        # the shrinking condition is when the target is immediately equal to or less than zero. I this case the window will need to be immediately decreased.

        # create a minimum_array_size element
        # create a current array size element 
        # most likely we can use target as the running total value within the loop.
        # create a left pointer value

        # create a for loop the incrementation variable will be the right pointer. Start the loop at index 1.
        # subtract right pointer value from target
        # increment current array size by one

        # conditional if target is equal to or less than zero check if current array size is less than minimum array size. if true overwrite minimum array size with current array size.
        # create a while loop that will break when target is not equal to zero
            # add right pointer value back to target
            # increment right pointer

        
        minimum_size = 0
        current_size = 0 
        left_pointer = 0

        for right_pointer in range(len(nums)):
            # print("right pointer value: ", nums[right_pointer], " left pointer value: ", nums[left_pointer], " target: ", target)
            # print("right pointer index: ", right_pointer, " left pointer index: ", left_pointer, " target: ", target)
            current_size += 1
            target -= nums[right_pointer]
            # print("current_size: ", current_size, " minimum size: ", minimum_size)

            if target <= 0:
                if current_size < minimum_size or minimum_size == 0:
                    minimum_size = current_size

                while left_pointer < len(nums) and target <= 0:
                    target += nums[left_pointer]
                    left_pointer += 1
                    current_size -= 1
                    if target <= 0:
                        if current_size < minimum_size:
                            minimum_size = current_size

        return minimum_size        