function isPalindrome(s: string): boolean {
    s = s.toLowerCase();
    s = s.replace(/[^a-z0-9]/g, "")
    let reversedString: string = s.split('').reverse().join('')
    return s === reversedString
};