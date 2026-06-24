class Solution:
    def numberOfArithmeticSlicesBruteforce(self, nums: List[int]) -> int:
        # key characteristics to keep in mind.
        ## the subarray will need to be at least three values long
        ## an arithmetic sequence will need to have the same difference value for all consecutive pairs.
        ## Will need to watch out for negative values 

        ## bruteforce method 
        # create a for loop that will keep track of i 
        # create a nested for loop that will keep track of j 
        # create a conditional that will keep track of the consecutive sequence. the sub array will need to be at least three values long for it to be considered.

        # time complexity can be interpreted as O(n^2)

        slices = 0 

        if len(nums) <= 2:
            return slices

        for i in range(len(nums) - 1):
            consecutive_diff = nums[i] - nums[i + 1]
            for j in range(i + 2, len(nums)):
                current_diff = nums[j - 1] - nums[j] 
                if current_diff == consecutive_diff and j - i + 1 >= 3:
                    slices += 1
                else:
                    break

        return slices