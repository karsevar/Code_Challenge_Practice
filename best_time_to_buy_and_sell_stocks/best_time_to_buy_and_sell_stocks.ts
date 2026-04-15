function maxProfitBruteForce(prices: number[]): number {
    // bruteforce solution
    let maximumProfit: number = 0
    for (let i: number = 0; i < prices.length - 1; i++) {
        for (let j: number = i+1; j < prices.length; j ++) {
            let currentProfit: number = prices[j] - prices[i] 
            if (maximumProfit < currentProfit) {
                maximumProfit = currentProfit
            }
        }
    }
    return maximumProfit
};

function maxProfit(prices: number[]): number {
    let maximumProfit: number = 0

    let minimumCost: number = prices[0]
    let i: number = 1

    while(i < prices.length) {
        let currentProfit: number = prices[i] - minimumCost
        if (currentProfit > maximumProfit) {
            maximumProfit = currentProfit
        }

        if (minimumCost > prices[i]) {
            minimumCost = prices[i]
        }
        i += 1
    }

    return maximumProfit
}