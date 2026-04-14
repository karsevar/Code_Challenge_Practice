function strStr(haystack: string, needle: string): number {
    const needleLength: number = needle.length;
    if (needleLength > haystack.length) {
        return -1
    }

    if (needleLength === haystack.length && needle === haystack) {
        return 0
    }
    console.log("extraction test: ", haystack.slice(1, 1+needleLength));

    for (let i: number = 0; i < (haystack.length - needleLength) + 1; i++) {
        if (needle === haystack.slice(i, needleLength+i)) {
            return i
        }
    }
    
    return -1
};