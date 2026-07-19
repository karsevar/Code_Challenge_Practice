class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # create a results array that will contain the permuations generated
        results = []

        # create a recursive function that will accept nums, start index, and state, and results as arguments
        self.permute_recursion(0, nums, results)

        # return results

        return results

    def permute_recursion(self, index: int, nums: List[int], results: List[List[int]]):
        # add state to results list

        # create a for loop that will start at index and end at len(nums)
        # recursively call permute_recursion
        # remove current index from state array

        if index == len(nums):
            if nums not in results:
                results.append(nums[:])

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.permute_recursion(index+1, nums, results)
            nums[index], nums[i] = nums[i], nums[index]