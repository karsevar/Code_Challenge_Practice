// Brute force solution
function twoSum(nums: number[], target: number): number[] {
    const indexes: number[] = [];
    for(let i: number = 0; i < nums.length - 1; i++) {
        for (let j: number = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                indexes.push(i);
                indexes.push(j);
            }
        }
    }

    console.log(indexes)
    return indexes
};

// Refined solution using hashmap
function twoSumHash(nums: number[], target: number): number[] {
    type TwoSumMap = Map<number, number>;
    const numsMap: TwoSumMap = new Map();

    for(let i: number = 0; i < nums.length; i++) {
        let difference: number = target - nums[i];

        if (numsMap.has(difference)) {
            return [numsMap.get(difference), i]
        } else {
            numsMap.set(nums[i], i)
        }
    }

    return []
}