function prefixConnected(words: string[], k: number): number {
    words = words.filter(word => word.length >= k);
    // okay so k should be regarded the length of the prefix so I'm required to evaluate each word one after another between indexes [0, k-1]. The most naive solution for this is to simply iterate through the words array and evaluate each word. 
    // create a hashmap that will effectively contain word[0:k-1] as the key and their corresponding words as the value. 
    // by the end of the function all I need to do is return the number of keys in the resoluting hashmap through [...prefixes.keys()].length. In fact there might be a convience function that will allow me to get that value.

    // initialize a prefixes hashmap that will contain all the possible prefixes in the words array. 

    // create a for loop that will iterate through the words array 
        // create a condition where if a words first k letters are not in the hashtable add that prefix key and the word in the values array. 
        // else just simply add the word to the values array of the prefix in question.

    // just simply return the number of keys in the hashtable

    const prefixes: Map<string, Array<string>> = new Map();
    console.log(words)

    if (words.length === 0) {
        return 0
    }

    for (let i = 0; i < words.length; i++) {
        // console.log("word: ", words[i].substring(0, k))
        let prefix: string = words[i].substring(0, k)
        if (!prefixes.has(prefix)) {
            prefixes.set(prefix, [words[i]])
        } else {
            let prefixWords: Array<string> = prefixes.get(prefix)
            prefixWords.push(words[i])
        }
    }

    let prefixCount: number = 0

    for (const [prefix, prefixWords] of prefixes) {
        if (prefixWords.length > 1) {
            prefixCount += 1
        }
    }
    return prefixCount
};