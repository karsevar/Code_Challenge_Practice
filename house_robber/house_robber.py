class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {
            len(nums): 0,
            len(nums)+1: 0,
            len(nums)+2: 0
        }
        return self.recursion_helper(
            0,
            nums,
            cache
        )
        
    
    def recursion_helper(self, index: int, nums: List[int], cache: dict[int, int]) -> int:
        if index in cache:
            return cache[index]

        skip = self.recursion_helper(index+1, nums, cache)
        take = nums[index] + self.recursion_helper(index+2, nums, cache)

        cache[index] = max(skip, take)
        return cache[index]
        