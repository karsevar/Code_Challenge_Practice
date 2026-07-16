class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Is problem seems straightforward. All we need to do is loop through the input array using k as the end of the window parameter. 

        # create a results array

        # create a for loop that will start at 0 and end at len(nums) - k + 1
        # for each iteration assess if the subset is a consecutive list of integers
        # if true add the sum to results array 
        # if false continue iterating through the nums array 


        results = []

        for i in range(len(nums) - k + 1):
            # print("nums[i:k]: ", nums[i:i+ k])
            if self.check_sorted(nums[i:i+k]):
                results.append(nums[i:i+k][-1])
            else:
                results.append(-1)

        return results


    def check_sorted(self, nums: List[int]) -> bool:
        first_value = nums[0]

        for index in range(1, len(nums)):
            first_value += 1
            if first_value != nums[index]:
                return False
        return True