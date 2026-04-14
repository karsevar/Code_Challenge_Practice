const cache: number[] = []

function climbStairs(n: number): number {
    if (n === 0) {
        return 1
    } else if (n < 0) {
        return 0
    }

    if (!cache[n]) { cache[n] = climbStairs(n - 1) + climbStairs(n - 2) }
    return cache[n]
};