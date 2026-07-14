class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # easiest solution to this is solving this problem in O(n + n) time where you will have to loop through the nums array once as a means to get the frequency of each number and a second loop where you check to see which number has the highest total frequency.

        # bruteforce: time complexity is O(n) and space complexity can be O(n) in the worst case where every number is unique.

        # how can we fix this solution?


        frequency_table = {}

        for num in nums:
            if num not in frequency_table:
                frequency_table[num] = 1

            else:
                frequency_table[num] += 1

        highest_frequency = 0 
        highest_num = None

        for num, frequency in frequency_table.items():
            if highest_frequency < frequency:
                highest_frequency = frequency 
                highest_num = num

        return highest_num
    
# Divide and conquer idea that solves this problem in O(nlogn) time complexity
class SolutionDivideAndConquer:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = self.majorityElementRec(nums, 0, len(nums) - 1)

        return candidate


        


    def majorityElementRec(self, nums: List[int], low, high) -> int:
        # print("\nmajorityElementRec function: low: ", low, " high: ", high, " nums[low]: ", nums[low], " nums[high]: ", nums[high])
        if low == high:
            return nums[low]

        mid = low + floor((high - low) / 2)
        # print("mid point: ", mid)

        leftMaj = self.majorityElementRec(nums, low, mid)
        rightMaj = self.majorityElementRec(nums, mid + 1, high)
        # print("leftMaj: ", leftMaj, " rightMaj: ", rightMaj)

        if leftMaj == rightMaj:
            return leftMaj

        leftCount = self.countOccurences(nums, low, high, leftMaj)
        rightCount = self.countOccurences(nums, low, high, rightMaj)

        # print("leftCount: ", leftCount, " rightCount: ", rightCount)

        if leftCount > rightCount:
            return leftMaj
        else:
            return rightMaj

    def countOccurences(self, nums: List[int], low: int, high: int, target: int) -> int:
        count = 0

        for i in range(low, high+1):
            if nums[i] == target:
                count += 1
        return count
