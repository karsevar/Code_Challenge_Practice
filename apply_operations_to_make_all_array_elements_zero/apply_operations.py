class Solution:
    # rough solution for this problem that uses recursion in a bruteforce manner to find 
    # whether or not an array can be made to be all zeros by subatracting 1 from k consecutive elements.
    # was able to get a solution that passes 606 out of 1029 test cases.
    def checkArray(self, nums: List[int], k: int) -> bool:
        # I think that a bruteforce backtrack solution can probably be used for this problem just get get a baseline solution working for all the base cases.

        # a solution is found if the return nums is equal to [0] * len(nums)

        # create a recursive function that will take in nums, k, and index. Most likely we will need to returns nums but will need to experiment a little bit.

        if self.recursion_helper(0, nums, k):
            return True
        return False

    def recursion_helper(self, index: int, nums: List[int], k: int):
        if [0] * len(nums) == nums:
            return True
        for i in range(index, len(nums) - k + 1):
            valid_sequence = True
            for j in range(k):
                if nums[i+j] <= 0:
                    valid_sequence = False
                    break

            if valid_sequence:
                for j in range(k):
                    nums[i+j] -= 1
                    
                if self.recursion_helper(
                    i,
                    nums,
                    k
                ):
                    return True

                for j in range(k):
                    nums[i+j] += 1

        return False


    # According to the editorial this is a greedy solution implementation and the time complexity is O(nk). Here's the ai link that describes the problem in more detail: https://chatgpt.com/share/6a85f267-bc0c-83e8-bb54-8e24945b2d33
    def checkArrayEditorial(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            
            if i + k > len(nums):
                return False

            amount = nums[i]

            for j in range(i, i + k):
                nums[j] -= amount

                if nums[j] < 0:
                    return False

        return True