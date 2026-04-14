function searchInsert(nums: number[], target: number): number {
    if (nums.length == 1) {
        if (nums[0] >= target) {
            return 0
        }
        return 1
    }
    for (let i: number = 0; i < nums.length - 1; i++) {
        let j: number = i + 1
        if (nums[i] < target && nums[j] >= target) {
            return j
        } else if (nums[i] >= target) {
            return i
        }
    }
    return nums.length
};