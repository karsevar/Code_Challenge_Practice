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