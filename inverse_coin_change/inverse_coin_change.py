class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        # okay so the maximum denomination value will be the length of the numWays array. And the values within the numWays array can be regarded as the number of instances within each sum combination. 
        # this can be solved as a backtracking problem where we have an outer loop that goes through the numWays index value and the numWays[index] value. These values will denote the total amount the denomination combination should sum into and the maximum length of the combination array.

        # we will need to create an outer for loop that will return the current index in the numWays array and the current numWays value.
        # we will need to create a recursive function that will take the numWays index plus one, the current numWays value, state which will be initialized as an empty array.

        # output for the recursive function will all the possible combinations 
        # we will need to add the possible combinations into a set as a means to remove duplicates.

        # return the set values as an array

        denominations = []

        for i in range(len(numWays)):
            cache = {}
            current = self.recursion_helper(
                0,
                i+1,
                denominations,
                cache,
            )

            if current == numWays[i]:
                continue
            
            if current +1 == numWays[i]:
                denominations.append(i+1)
                continue
            
            return []

        return denominations

    def recursion_helper(self, index: int, amount: int, coins: List[int], cache: dict[tuple[int], int]):
        if amount == 0:
            return 1
        if amount < 0:
            return 0 

        if index >= len(coins):
            return 0

        if (amount, index) in cache:
            return cache[(amount, index)]

        take = self.recursion_helper(
            index,
            amount - coins[index],
            coins,
            cache,
        )

        skip = self.recursion_helper(
            index+1,
            amount,
            coins,
            cache,
        )

        cache[(amount, index)] = take + skip

        return cache[(amount, index)]