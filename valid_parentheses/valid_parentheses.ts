function isValid(s: string): boolean {
    const closingBracketsMap: Map<string, string> = new Map([
        [ ")", "("],
        ["]", "["],
        ["}", "{"]
    ]);

    const openingBracketsMap: Map<string, string> = new Map([
        ["(", ")"],
        ["[", "]"],
        ["{", "}"]
    ]);

    const bracketStack: string[] = [];
    if (s.length <= 1) {
        return false
    }

    bracketStack.push(s[0])

    let bracketIndex: number = 1

    while (bracketIndex < s.length) {
        if (openingBracketsMap.has(s[bracketIndex])) {
            bracketStack.push(s[bracketIndex])
        } else if (closingBracketsMap.has(s[bracketIndex])) {
            if (bracketStack.length >= 1) {
                let lastElement: string | undefined = bracketStack.pop();
                if (openingBracketsMap.has(lastElement) && openingBracketsMap.get(lastElement) === s[bracketIndex]) {
                    continue
                } else {
                    return false
                }
            } else {
                return false
            }
        }
        bracketIndex += 1
    }

    if (bracketStack.length > 0) {
        return false
    }

    return true
};