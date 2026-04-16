function topKFrequent(words: string[], k: number): string[] {
    // first of all we will need to create a hash map that will keep track of the words and their frequency. 

    // create a hashmap 

    // create a for loop that will iterate through words and populate the hash map with each word and their count within the array.
    
    // create an array of arrays variable called bucket that will reorganize the words and their frequencies as such.
    // bucket = [["word", "word2"], ....]
    // bucket: index == word count

    // create a variable called res that will keep track of the words that are the highest frequency.

    // loop through the bucket array from the last index to the first index since the last index will carry an array that have the words with the highest frequency. 
    
    // return res

    let n: number = words.length
    const freqHash: Map<string, number> = new Map()

    for (let i: number = 0; i < words.length; i++) {
        if (freqHash.has(words[i])) {
            let count: number = freqHash.get(words[i])
            count += 1
            freqHash.set(words[i], count)
        } else {
            freqHash.set(words[i], 1)
        }
    }

    const bucket: Array<Array<string>> = Array(n + 1).fill(null).map(() => []);

    for (let [word, freq] of freqHash) {
        bucket[freq].push(word)
    }

    console.log(freqHash)
    console.log(bucket)

    const res: Array<string> = []

    let kCount: number = 0
    for (let freq: number = bucket.length-1; freq >= 0; freq--) {
        if (kCount === k) {
            break
        }

        if (bucket[freq].length !== 0) {
            let bucketArray: Array<string> = bucket[freq].sort()
            for (let freqIndex = 0; freqIndex < bucket[freq].length; freqIndex++) {
                if (kCount < k) {
                    res.push(bucket[freq][freqIndex])
                    kCount += 1
                } else if(kCount === k) {
                    break
                }
            }   
        }
    }

    return res
};