function plusOne(digits: number[]): number[] {
    let addOne: number = 1;
    const newDigits: number[] = []

    for (let i: number = digits.length - 1; i >= 0; i--) {
        let newSum: number = digits[i] + addOne;
        if (newSum == 10) {
            newDigits.unshift(0)
            addOne = 1
        } else {
            addOne = 0
            newDigits.unshift(newSum)
        }
    }

    if (addOne == 1) {
        newDigits.unshift(1)
    }

    return newDigits;
};