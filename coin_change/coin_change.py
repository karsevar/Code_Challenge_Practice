import math

class Solution:
    # bruteforce method. I'm primarily iterating through the coins array multiple times to kind the path 
    # in which has the least amount of coins. The way I structured the recursion function kind of keeps me 
    # from simplifying the time complexity more through adding memoization through a cache.
    def coinChange(self, coins: List[int], amount: int) -> int:
        # the first course of action is to set up the recursion pattern dynamic programming. we are given all the possible coin denominations and we can use each denomination more than once. 
        # okay so in the recursion function we can create a loop that will go through each denomination in sequence.
        # the base case will be if amount is equal to 0. If this is true than return 1 if not return a very high value.

        # cache[amount] = count. This seems like an okay cache solution except I think that we may need to contend with denomination combinations that might create a similar count amount. 

        minCount = self.recursion_helper(
            0,
            coins,
            amount,
            0,
        )

        return minCount if minCount != float("inf") else -1

    def recursion_helper(
        self,
        index: int,
        coins: List[int],
        amount: int,
        count: int,
    ) -> int:
        if amount == 0:
            return count
        elif amount < 0:
            return float("inf")

        minCount = float("inf")
        
        for i in range(index, len(coins)):
            currentCount = self.recursion_helper(
                i,
                coins,
                amount-coins[i],
                count+1
            )

            if minCount > currentCount:
                minCount = currentCount

        return minCount




class SolutionCache:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        minCount = self.recursion_helper(
            coins,
            amount,
            cache,
        )

        print("cache: ", cache)

        return minCount if minCount != float("inf") else -1

    def recursion_helper(
        self,
        coins: List[int],
        amount: int,
        cache: dict[int, int]
    ) -> int:
        if amount == 0:
            return 0
        elif amount < 0:
            return float("inf")

        if amount in cache:
            return cache[amount]

        min_count = float("inf")
        
        for coin in coins:
            remaining_coins = self.recursion_helper(
                coins,
                amount-coin,
                cache
            )

            current_count = 1 + remaining_coins

            min_count = min(
                min_count,
                current_count
            )

        cache[amount] = min_count

        return min_count