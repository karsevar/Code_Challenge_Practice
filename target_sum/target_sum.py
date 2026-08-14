class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # okay the straightforward way is to use backtracking to figure out the number of combinations required to get to the target value.
        # the main question is whether to use a positive sign or a negative sign.

        # create a results array
        
        # return the length of the results array

        visited = {}

        return self.recursion_helper(
            0,
            0,
            nums,
            target,
            visited
        )

    def recursion_helper(
        self,
        index: int,
        current_sum: int,
        nums: List[int],
        target: int,
        visited
    ):

        if index == len(nums):
            if current_sum == target:
                return 1
            return 0

        if (index, current_sum) in visited:
            return visited[(index, current_sum)]

        positive_result = self.recursion_helper(
            index + 1,
            current_sum + nums[index],
            nums,
            target,
            visited
        )



        negative_result = self.recursion_helper(
            index + 1,
            current_sum - nums[index],
            nums,
            target,
            visited
        )

        visited[(index, current_sum)] = positive_result + negative_result

        return visited[(index, current_sum)]