class Solution:
    # The bruteforce method passed 54 of the 61 test cases. It seems that I didn't have to discount the last element in the array for the outer loop since there can be subarrays with only one element in the solution. Time complexity can be interpreted as O(n^2) since I am looping through nums twice.
    def numSubarraysWithSumBruteforce(self, nums: List[int], goal: int) -> int:
        # so the idea is that the length of the possible subarrays is dictated by the input goal value. meaning that if goal was 1 then the subarray list can contain some values that are of length one as well.

        # to make things a little more straightforward, I will first attempt to use the bruteforce method to answer this question.

        # to begin I will need to create a subarray_count variable that will keep track of all the subarrays that equal into the goal value.

        # create a for loop that will keep track of index i (the starting point for the subarray)
        # initialize a current count variable that will keep track of the number of ones the loop runs into.
        # create a nested for loop that will keep track of index j
        # add index j value to the current count variable
        # create a conditional that will check the current count reached the goal value
        # if so iterate the subarray_count variable by one
        # if the current count is higher than the goal value break the loop.

        subarray_count = 0

        for i in range(len(nums)):
            current_count = nums[i]
            if current_count == goal:
                subarray_count += 1
            for j in range(i + 1, len(nums)):
                current_count += nums[j] 
                if current_count == goal:
                    subarray_count += 1
                elif current_count > goal:
                    break

        return subarray_count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # The only other optimization that I can think of is using the dynamic sliding window technique with the main difference being the incrementation of the left pointer. Most cases the left pointer will be incremented in order to make the subarray count equal to the goal value but I believe that perhaps we might need to continue incrementing the left pointer even if the goal is reached.

        subarray_count = 0
        current_count = 0
        frequency = 0
        left = 0

        for right in range(len(nums)):
            current_count += nums[right]
            if nums[right] == 1:
                frequency = 0
            if current_count > goal:
                current_count -= nums[left]
                left += 1

            while left <= right and current_count == goal:
                current_count -= nums[left]
                left += 1
                frequency += 1
            subarray_count += frequency

        return subarray_count