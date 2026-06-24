class Solution:
    # brutefore method was able to pass 170 out of 208 test cases
    # time complexity O(n^2)
    def findLHSBruteforce(self, nums: List[int]) -> int:
        # the first example seems to go against the idea of retaining the original ordering of the nums array since they are discounting the 5 in the first example solution.

        # first sort the array

        nums = sorted(nums)
        # print("nums", nums )
        max_len = 0 

        # first I should just use the bruteforce method
        # create a for loop that will keep track of index i 
        # create another for loop that will keep track of index j 
        # conditional check that the difference between index i and j is equal to one. if true check if i + j + 1 is greater than maximum length value.

        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if (nums[j] - nums[i]) == 1:
                    max_len = max(max_len, (j - i) + 1)
        return max_len

    def findLHS(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_len = 0
        left = 0

        for right in range(1, len(nums)):
            current_diff = nums[right] - nums[left]

            while current_diff > 1:
                left += 1
                if left == right:
                    break
                current_diff = nums[right] - nums[left]

            if current_diff == 1:
                max_len = max(max_len, (right - left) + 1)

        return max_len