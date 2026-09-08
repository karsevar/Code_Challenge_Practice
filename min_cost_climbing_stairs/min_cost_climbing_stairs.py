class Solution:
    ## Bruteforce solution for this problem Exceeds time limit at test case 259. 
    # The time complexity is exponential O(2n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # okay it seems that we will need to keep track of the 
        # index for each recursion chain and also increment the cost of each of each recursion chain and process which has the lowest cost.
        # unlike the other problems we are incrementing through the input array and not an n value directly.

        # we can take either one or two steps each iteration in the loop 

        # bruteforce create a recursion function that will take in the following arguments cost_array, cost integer that will be used as a tally for each recursive step, index which we can either increment by one or two index positions

        return min(
            self.recursion_helper(
                cost,
                0,
                0
            ),
            self.recursion_helper(
                cost,
                0,
                1
            )
        )

    def recursion_helper(
        self,
        cost_array: List[int],
        cost: int,
        index: int,
    ) -> int:
        min_cost = float("inf")
        if index >= len(cost_array):
            return cost

        else:
            one_step_cost = self.recursion_helper(
                cost_array,
                cost+cost_array[index],
                index+1
            )

            min_cost = min(one_step_cost, min_cost)

            two_step_cost = self.recursion_helper(
                cost_array,
                cost+cost_array[index],
                index+2
            )

            min_cost = min(two_step_cost, min_cost)

        return min_cost


## Cache solution technically this should decrease the time complexity to O(n) though given that I'm still 
# calling the recursive function twice at the beginning the time complexity might be a little more.
# Will need to clean this implementation and little more.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # okay it seems that we will need to keep track of the 
        # index for each recursion chain and also increment the cost of each of each recursion chain and process which has the lowest cost.
        # unlike the other problems we are incrementing through the input array and not an n value directly.

        # we can take either one or two steps each iteration in the loop 

        # bruteforce create a recursion function that will take in the following arguments cost_array, cost integer that will be used as a tally for each recursive step, index which we can either increment by one or two index positions

        cache = {
            len(cost): 0,
            len(cost)+1: 0,
            len(cost)+2: 0,
        }

        return min(
            self.recursion_helper(
                cost,
                0,
                cache
            ),
            self.recursion_helper(
                cost,
                1,
                cache
            )
        )

    def recursion_helper(
        self,
        cost: List[int],
        index: int,
        cache: dict[int, int]
    ) -> int:
        if index in cache:
            return cache[index]

        cache[index] = cost[index] + min(
            self.recursion_helper(cost, index+1, cache),
            self.recursion_helper(cost, index+2, cache)
        )

        return cache[index]