class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #     # The bruteforce solution is to simply loop through the array twice and calculate which combination has the highest return on investment.

    #     # create a variable that will carry the highest profit during the duration of the nested loops.
    #     # create a for loop that will go from the first index and end at the second to last index.
    #         # create another for loop that will go from i to the last index in the array.
    #             # discount any combination where the value in jth index is lower than value in ith index.
    #             # subtract value in jth index with ith index
    #             # check if this value is higher than the recorded highest profit variable.


        highest_profit = 0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    if profit > highest_profit:
                        highest_profit = profit

        return highest_profit

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minCost = prices[0]
        i = 1

        while i < len(prices):
            current_profit = prices[i] - minCost
            if current_profit > profit:
                profit = current_profit
            
            if minCost > prices[i]:
                minCost = prices[i]
            i += 1
        return profit