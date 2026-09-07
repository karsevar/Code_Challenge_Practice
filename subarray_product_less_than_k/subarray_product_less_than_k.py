class Solution:
    # The time complexity for this problem can be conceptualized as O(n) since technically we are only looping 
    # through the array once. And the space complexity can be conceptualized as O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left_pointer = 0
        current_product = 0
        subarray_count = 0

        for right_pointer in range(len(nums)):
            if current_product == 0:
                current_product = nums[right_pointer]
            else:
                current_product *= nums[right_pointer]
            
            while left_pointer <= right_pointer and current_product >= k:
                current_product = current_product/nums[left_pointer]
                left_pointer += 1

            subarray_count += right_pointer - left_pointer + 1

        return subarray_count