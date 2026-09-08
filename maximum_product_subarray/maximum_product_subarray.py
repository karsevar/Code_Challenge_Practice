import math 

## Bruteforce method that goes through all the possible combinations within the input array to get the 
# maximum possible product. This is by far the worst time complexity solution since we are assessing every possible 
# combination which increases it to the factorial range. Currently this solution is not passing test case 183
# due to exceeding time limit.
import math 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.recursion_helper(
            0,
            nums
        )
        

    def recursion_helper(self, index: int, nums: List[int]) -> int:

        max_product = float("-inf")

        for i in range(index, len(nums)):
            current_product = math.prod(nums[index:i+1])
            max_product = max(
                max_product,
                current_product
            )
            recursive_max = self.recursion_helper(
                i+1,
                nums
            )

            max_product = max(
                max_product,
                recursive_max
            )

        return max_product