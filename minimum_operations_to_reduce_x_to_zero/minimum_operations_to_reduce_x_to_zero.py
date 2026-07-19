class Solution:
    # First attempt only passes 43 of the 97 test cases. This solution uses dynamic sliding window while also sorting the input nums array. It seems that this is not correct way to do this since we are missing some combinations that sorting the array overlooks.
    def minOperations(self, nums: List[int], x: int) -> int:
        # wait a second we can get around having to use recursive permuation backtracking through just simply ordering the array from least to greatest before using a dynamic window approach. 

        # first sort the input array
        # create a minimum operations count variable initialize to -1
        # create a current operations count variable initialize to 0
        # create a left pointer variable initialized to the first index in array

        # create a for loop that will have right_pointer variable name for the iterator
        # substract nums[right_pointer] from the x variable
        # increment current operations count variable by one

        # check if x variable is equal to zero if true check if minimum operations is greater than current operations
        # if true overwrite minimum operations with current operations

        # check if x variable is less than zero if true create a while loop that will terminate when x is greater than zero 
        # make sure to add nums[left_pointer] back into x, increment left_pointer by one, and decrement current operations by one

        nums = sorted(nums)

        minimum_operations = -1
        current_operations = 0
        left_pointer = 0

        print("nums: ", nums)

        for right_pointer in range(len(nums)):
            x -= nums[right_pointer]
            current_operations += 1
            print("\nnums[left_pointer]: ", nums[left_pointer], " nums[right_pointer]: ", nums[right_pointer], " x: ", x)

            if x == 0:
                if current_operations < minimum_operations or minimum_operations == -1:
                    minimum_operations = current_operations

            elif x < 0:
                while left_pointer < right_pointer and x < 0:
                    x += nums[left_pointer]
                    left_pointer += 1
                    current_operations -= 1
                    print("in while loop nums[left_pointer]: ", nums[left_pointer], " nums[right_pointer]: ", nums[right_pointer], " x: ", x)
                if x == 0:
                    if current_operations < minimum_operations or minimum_operations == -1:
                        minimum_operations = current_operations

        return minimum_operations
    
class Solution:
    # Editorial solution: Will need to read more on prefix sums
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        max_len, cur_sum, left = 0, 0, 0

        if target == 0:
            return len(nums)


        for right in range(len(nums)):
            cur_sum += nums[right]

            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == 0 else len(nums) - max_len