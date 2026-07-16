class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # This seems to be just like all the other combination sum problems. 
        # I will use the same logic as all of my other submissions.

        # this case we only need a results counter in place of a results array
        visited = {}

        return self.combination_helper([], nums, target, visited)

    def combination_helper(self, state: List[int], nums: List[int], target: int, visited) -> int:
        # base case if target is equal to zero iterate results counter by one and return null
        # base case if target is less than zero return null only

        # since we are able to count the same number in the array more than once and order of the sequence matters we can create a for loop that will start at the zero index and end at len(nums) - 1.
        # print("state: ", state, " target: ", target, " visisted: ", visited)
        if target == 0:
            return 1
        if target < 0:
            return 0

        if target in visited:
            return visited[target]

        results = 0

        for choice in nums:
            state.append(choice) 
            results += self.combination_helper(state, nums, target - choice, visited)
            state.pop()

        visited[target] = results
        return results