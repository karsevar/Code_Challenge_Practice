class Solution:
    # time complexity can be interpreted as O(n) since we are only looping through the nums array once and compiling the hashmap in that single loop.
    # Space complexity can be O(n) in the worst case if all the remainder calculations are unique.
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # according to the algorithm specifications I need to create a frequency hashmap that will contain the counts of each subarray sum. According to the prompt I only have to document the remainder in the hashmap since I'm only documenting subarrays that are divisible by k and not sum up to k.

        # create a hashmap 
        freq = {0: 1}
        # create a count variable
        count = 0
        # create running sum variable
        running_sum = 0

        # create a for loop that will go through nums
        # if running_sum % k in freq increment count
        # add remainder to the prefix sum frequency hashmap 
        # return count

        for num in nums:
            running_sum += num
            if (abs(running_sum % k)) in freq:
                count += freq[abs(running_sum % k)]
            
            freq[running_sum % k] = freq.get(running_sum % k, 0) + 1 

        return count