function longestCommonPrefix(strs: string[]): string {
    // The bruteforce solution is to simply create two loops.
    // One loop that will cycle through the words in the array and the second that will loop through
    // the individual characters. Or perhaps the other way around. 

    // initialize a common prefix variable that will begin as an empty string

    // create a for loop that will loop through all the characters from the shortest word

    // create a nested for loop that will loop through all the words in the array. 

    let prefix: string = ""

    if (strs.length === 1) {
        return strs[0]
    } 

    if (strs.length === 0) {
        return prefix
    }

    for (let i = 0; i < strs[0].length; i++) {
        for (let word = 0; word < strs.length; word++) {
            if (strs[word][i] !== strs[0][i]) {
                return prefix
            }
        };
        prefix += strs[0][i]
    };
    return prefix
};