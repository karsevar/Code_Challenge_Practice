class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums) 
        self.solve(n, 0, nums, [], results)
        print("results: ", results)

    def solve(self, n: int,  i: int, nums: List[int], sequence: List[int], results: List[List[int]]):
        if i == n:
            print("sequence: ", sequence, " index: ", i)
            results.append(sequence[:])
            return 

        sequence.append(nums[i])
        self.solve(n, i+1, nums, sequence, results)
        sequence.pop()
        self.solve(n, i+1, nums, sequence, results)