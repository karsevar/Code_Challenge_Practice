class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # okay according to the editorial I will need to keep from of the earliest index in which a specific remainder was found.

        # The conditional that was used to increment the counter can be used to return true if the current subarray has a length greater than 2. 

        # create a hashmap that will keep track of the remainder as a key and the earliest index as the value.

        # create a value that will keep track of the cumulative sum

        # create a for loop that will loop through the nums array.
        # add nums[i] to the cumulative sum
        # check if cumulative sum % k remainder can be found in hashmap
        # if true check if earliest index - current index is greater than one
            # if true return true

        # Add remainder to hashmap and the current index as a value

        freq = {0: -1}
        total_sum = 0

        for i in range(len(nums)):
            total_sum += nums[i]
            remainder = total_sum % k
            if remainder in freq:
                earliest_index = freq[remainder]
                if i - earliest_index > 1:
                    return True
            else:
                freq[remainder] = i

            print("\n")

        return False