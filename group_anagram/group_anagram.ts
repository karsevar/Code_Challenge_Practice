function groupAnagrams(strs: string[]): string[][] {
    // By far the bruteforce method that comes to mind for this problem is to create a hashtable that will keep track of each of the anagrams. The key will be the alphabetically converted anagram string.
    // example of hashmap 
    // "aet": ["eat", "ate", "tea"]

    // The issue with this method is that we will be forced to use the split string method and the sort method and then the join method for each part of key creation and anagram placement in their corresponding arrays. 
        // sorting and array conversion methods upon each loop iteration can increase time complexity if the words in question are unusually large.

    // bruteforce method

    // initialize a hashmap that will have alphebetically sorted anagram of a word as a key and an array of all corresponding words as a value.
    // for loop iterate over strs
        // sort string into alphebetically ordered anagram string
        // check if sorted anagram string can be found in the hashmap
            // if not add the alphebetically sorted string as a key and the corresponding word in the value's array.
            // if the sorted anagram string is found just simply add the string to the value's array.

    // returning the values can be simply using the [...hashmap.values()] command

    const anagramMap: Map<string, Array<string>> = new Map()

    for (let i: number = 0; i < strs.length; i++) {
        let alphaString: string = strs[i].split("").sort().join("");
        if (anagramMap.has(alphaString)) {
            let anagramList: string[] | undefined = anagramMap.get(alphaString)
            anagramList!.push(strs[i])
        } else {
            anagramMap.set(alphaString, [strs[i]])
        }
    }

    // console.log(anagramMap)

    return [...anagramMap.values()]
};