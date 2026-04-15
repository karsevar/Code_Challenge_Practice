function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    
    while (nums2.length > 0) {
        let num2Value: number | undefined = nums2.shift()
        m += 1
        for (let i: number = 0; i < nums1.length; i++) {
            if (num2Value === undefined) {
                break
            }
            if (num2Value < nums1[i]) {
                let iValue: number = nums1[i]
                nums1[i] = num2Value
                num2Value = iValue
            } else if (nums1[i] === 0 && i >= m - 1) {
                nums1[i] = num2Value
                break
            }
        }
    }
};