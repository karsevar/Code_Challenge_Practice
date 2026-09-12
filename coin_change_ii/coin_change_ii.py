class SolutionBacktrack:
    # used the back tracking alorithm to solve this problem using bruteforce time complexity. It's important to keep in mind that this solution most likely has a higher time complexity than O(n^2) given that I'm going through every possible combination and that I'm taking on an additional time complexity hit through sorting the state array everytime the amount reaches zero and I'm looping through the results array just to see if that one state array is already accounted for. 
    def change(self, amount: int, coins: List[int]) -> int:
        # this seems like another counting problem where the base case is when the amount equals zero we will return 1 since that combination is valid while any amount that is less than zero will return a zero since that combination is invalid.
        # We can loop through a specific denomination multiple times according to the prompt.

        results = []

        self.recursion_helper(
            amount,
            coins,
            [],
            results
        )

        return len(results)

    def recursion_helper(
        self,
        amount: int,
        coins: List[int],
        state: List[int],
        results: List[List[int]]
    ):
        if amount == 0:
            sorted_state = sorted(state[:])
            if sorted_state not in results:
                results.append(sorted_state)
            return 
        
        if amount < 0:
            return 

        for coin in coins:
            state.append(coin)
            self.recursion_helper(
                amount - coin,
                coins,
                state,
                results
            )
            state.pop()


class SolutionOptimized:
    # it seems that after reading some tutorials on this problem the take and skip pattern works by
    # keeping the combinations from not being assessed multiple times unlike my implementation before.
    # Will need to look more into the logic on why (amount, index) works as the correct keys to the cache.
    def change(self, amount: int, coins: List[int]) -> int:

        results = []

        cache = {}

        return self.recursion_helper(
            0,
            amount,
            coins,
            cache,
        )

    def recursion_helper(
        self,
        index: int,
        amount: int,
        coins: List[int],
        cache: dict[int, int]
    ):
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
            cache
        )

        skip = self.recursion_helper(
            index+1, 
            amount,
            coins,
            cache
        )

        cache[(amount, index)] = take + skip

        return cache[(amount, index)]