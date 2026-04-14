function lengthOfLastWord(s: string): number {
    let stringArray: Array<string> = s.trim().split(/\s+/);

    if (stringArray.length === 0) {
        return 0
    }

    return stringArray[stringArray.length - 1].length
};