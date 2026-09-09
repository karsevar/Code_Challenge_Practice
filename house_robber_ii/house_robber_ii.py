class Solution:
    # Had to get a little help with coming up with this solution. It seems that excluding either the first or
    # last house in the array is the best way to reason about this problem as it is not possible for a solution
    # to have values of both the first and last house.

    # Roughly the time complexity can be computed as O(n) and space complexity can be regarded as O(n) as well
    def rob(self, nums: List[int]) -> int:
        # since the houses form a circle around one another we will need to modify the algorithm in such a way that when the loop reaches the end of the array the last index it will reset to the first index. 
        # issue with this is that we will create an infinite loop if we don't handle the stop condition correctly.

        # create a recursive function that will work in much the same way as the last neighbors solution
        # arguments will be index, nums to start and we will modify the solution with a cache once we understand the principles of the circle modifications

        if len(nums) <= 1:
            return nums[0]

        return max(
            self.recursion_helper(
                    0,
                    nums[1:],
                    {}
                ),
            self.recursion_helper(
                    0,
                    nums[:-1],
                    {}
                ),
        )

    def recursion_helper(self, index: int, nums: List[int], cache: dict[int, int]) -> int:
        if index >= len(nums):
            return 0

        if index in cache:
            return cache[index]

        skip = self.recursion_helper(
            index+1,
            nums,
            cache
        )

        take = nums[index] + self.recursion_helper(
            index+2,
            nums,
            cache
        )

        cache[index] = max(skip, take)
        return cache[index]
        # return max(skip, take)
        