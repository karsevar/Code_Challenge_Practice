// Initial attempt using typescript

function threeSum(nums: number[]): number[][] {
    // Not working with most of the leetcode test cases.
    nums.sort((a, b) => a - b)
    const sumSet: Set<number> = new Set();

    const threeSumCombinations: Set<string> = new Set()

    for (let i: number = 0; i < nums.length-1; i++) {
        for (let j: number = i + 1; j < nums.length; j++) {
            let twoSum: number = nums[i] + nums[j];
            let difference: number = 0 - twoSum;

            // console.log("difference: ", difference)
            // console.log("twoSum value: ", twoSum)

            if (sumSet.has(difference)) {
                    threeSumCombinations.add(
                        JSON.stringify([nums[i], nums[j], difference].sort())
                    );
            } else {
                sumSet.add(nums[i])
            }
        }
    }

    console.log("threeSumCombinations: ", threeSumCombinations)
    console.log("sumSet values: ", sumSet)

    return Array.from(
        threeSumCombinations,
        (item) => JSON.parse(item)
    )
};

// It seems that it isn't efficient enough to pass the last edge case but it is the closest solution that I can think up.
function threeSumFixed(nums: number[]): number[][] {
    nums.sort((a, b) => a - b)

    const threeSumCombinations: Set<string> = new Set()

    for (let i: number = 0; i < nums.length-1; i++) {
        const sumSet: Set<number> = new Set();

        for (let j: number = i + 1; j < nums.length; j++) {
            let twoSum: number = nums[i] + nums[j];
            let difference: number = 0 - twoSum;

            // console.log("difference: ", difference)
            // console.log("twoSum value: ", twoSum)

            if (sumSet.has(difference)) {
                    threeSumCombinations.add(
                        JSON.stringify([nums[i], nums[j], difference].sort())
                    );
            }

            sumSet.add(nums[j])
        }
    }

    // console.log("threeSumCombinations: ", threeSumCombinations)

    return Array.from(
        threeSumCombinations,
        (item) => JSON.parse(item)
    )
};