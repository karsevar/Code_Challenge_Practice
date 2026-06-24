class Solution:
    # bruteforce method passed 83 of the 93 test cases. 
    # time complexity is O(n^2)
    def subarraySumBruteforce(self, nums: List[int], k: int) -> int:
        # First let's use the bruteforce method to solve this problem

        # create a subarray count variable 
        
        # create a for loop that will keep track of i
        # initialize the current count variable with nums[i] 
        # create a for loop that will keep track of j
        # check if current count is equal to k 
        # if true iterate subarray count variable
        

        subarray_count = 0

        for i in range(len(nums)):
            current_sum = nums[i]
            if current_sum == k:
                subarray_count += 1
            for j in range(i + 1, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    subarray_count += 1
        
        return subarray_count

    def subarraySumHashtable(self, nums: List[int], k: int) -> int:
        # the most straightforward solution is to use a hash table to solve this problem using 0(n) time complexity and O(n) space complexity.

        # create a hash table that looks like this during run time
        # {remainder: nums[i] value}

        frequency_table = {0: 1}
        current_sum = 0
        subarray_count = 0

        for num in nums:
            current_sum += num
            remainder = current_sum - k

            if remainder in frequency_table:
                subarray_count += frequency_table[remainder]
            
            if current_sum in frequency_table:
                frequency_table[current_sum] += 1
            else:
                frequency_table[current_sum] = 1

        return subarray_count

    # it seems that the dynamic window method is not a good fit for this problem as the left pointer will be incremented whenever the current sum is greater than k thus making test case 3 fail without a large amount of intervening logic.
    def subarraySumWindow(self, nums: List[int], k: int) -> int:
        current_sum = 0
        subarray_count = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            print("current_sum: ", current_sum)
            print("left pointer: ", left, " right pointer: ", right)

            while left <= right and current_sum > k:
                current_sum -= nums[left]
                left += 1

            if current_sum == k:
                subarray_count += 1

        return subarray_count