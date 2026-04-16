function topKFrequent(nums: number[], k: number): number[] {
    // bruteforce method with a hashtable

    let frequencyHash: Map<number, number> = new Map()

    let highestValues: Map<number, number> = new Map()

    for (let i = 0; i < nums.length; i++) {
        if (!frequencyHash.has(nums[i])) {
            frequencyHash.set(nums[i], 1)
        } else {
            let count: number = frequencyHash.get(nums[i])
            count += 1
            frequencyHash.set(nums[i], count)
        }
    }

    for (let [key, value] of frequencyHash) {
        // console.log("highest values: ", highestValues)
        if (highestValues.size < k) {
            highestValues.set(key, value)
        } else {
            let keyToDelete: number = key
            let valueToDelete: number = value
            // console.log("key: ", key, "value: ", value)
            for (let [highKey, highValue] of highestValues) {
                // console.log("keyToDelete: ", keyToDelete, "valueToDelete: ", valueToDelete)
                // console.log("highKey: ", highKey, "highValue: ", highValue)
                if (highValue < valueToDelete) {
                    keyToDelete = highKey
                    valueToDelete = highValue
                }
            }
            if (keyToDelete !== key) {
                highestValues.delete(keyToDelete)
                highestValues.set(key, value)
            }
        }
    }

    // console.log("frequencyHash: ", frequencyHash)
    // console.log("highest values: ", highestValues)
    return [...highestValues.keys()]
};

// Nice solution but I was slower than my initial solution.
function topKFrequentEditorial(nums: number[], k: number): number[] {
    // bruteforce method with a hashtable

    let n: number = nums.length;
    const occur: Map<number, number> = new Map()

    for (let num: number = 0; num < nums.length; num++) {
        if (occur.has(nums[num])) {
            let count: number = occur.get(nums[num])
            count += 1
            occur.set(nums[num], count)
        } else {
            occur.set(nums[num], 1)
        }
    }

    let bucket: Array<Array<number>> = new Array(n + 1).fill(null).map(() => []);

    console.log("bucket: ", bucket)
    console.log("occur: ", occur)

    for (const [key, value] of occur) {
        console.log("key: ", key, "value: ", value)
        let array: Array<number> = bucket[value]
        array.push(key)
    }

    console.log("bucket: ", bucket)

    let res: Array<number> = []

    for (let i: number = n; 0 <= i; i--) {
        if (res.length >= k) {
            break
        }
        for (let valueIndex: number = 0; valueIndex < bucket[i].length; valueIndex++) {
            res.push(bucket[i][valueIndex])
        }
    }

    return res
};