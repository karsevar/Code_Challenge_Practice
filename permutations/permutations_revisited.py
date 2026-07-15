# Time complexity for this problem is O(n!) since I'm looking up all possible combinations.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # okay the integers in nums are all unique and the length of nums will only be up to 6. 

        # the main difference between this problem and all the other problems is that I need to keep order in mind and that I will need to define a visited set that will keep track of all the visited permuations. I think I will keep visited and solutions separate for now.

        # create a visited set and solutions array

        # create a function that will be used as the recursive function. visited and solutions will be passed into the function as arguments as well as nums.

        # return solutions

        visited = set()
        solutions = []

        self.backtrack_helper([], nums, visited, solutions)

        # print("solutions: ", solutions)
        # print("visited: ", visited)
        return solutions

    def backtrack_helper(self, state: List[int], nums: List[int], visited: set[int], solutions: List[List[int]]):
        # base case: if state has length of nums and is not in visited
        # copy state into solutions 

        # create loop for nums: example for choice in nums
        # check if state is not in visited
        # if true add choice to state and call backtrack function and then pop() last value from state

        state_set = " "
        if len(state) > 0:
            state_set = str(state)
        
        # print("state: ", state)
        # print("state_set: ", state_set)

        if len(state) == len(nums) and state_set not in visited:
            solutions.append(state[:])
            visited.add(state_set)
            return

        for choice in nums:
            if choice not in state:
                state.append(choice)
                self.backtrack_helper(state, nums, visited, solutions)
                state.pop()

# first attempt. It really isn't the most optimized solution since I'm going through each individual combination multiple times. Most likely a visited cache will optimize this a little more with some sacrefice to space complexity.
class SolutionAttemptTwo:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # since the order and size of the permutations matter in this exercise I believe that I can use the same method as the combinations exercise with slight modifications. 

        # namely the base case should check if the subset size equals the size of the passed in nums array and if the permutation is already represented in the output results array.

        # create results array

        # call recursive function that will take results, nums, and state as arguments. 

        # return results

        # create a visited set where we can contain all visited paths.
        # visited example: set(" ", "2 3")

        # print(" ".join([str(int_str) for int_str in []]))
        # adding a set as a cache only increased the speed of the algorithm about 20 percent compared to my previous method. At least I was able to remove the state not in results check which is a good benefit of this modification.

        results = []
        visited = set()
        self.permute_helper(visited, [], nums, results)
        return results

    def permute_helper(self, visited, state: List[int], nums: List[int], results: List[List[int]]):
        # print(" state: ", state, " visited: ", visited)
        path = " ".join([str(int_str) for int_str in state])

        if path not in visited:
            visited.add(path)
            if len(state) == len(nums):
                results.append(state[:])
                return

            for choice in range(len(nums)):
                if nums[choice] not in state:
                    state.append(nums[choice])
                    self.permute_helper(visited, state,  nums, results)
                    state.pop()