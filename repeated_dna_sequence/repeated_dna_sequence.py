class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # time complexity can be calculated as O(n) since I'm looping through the s string once and looping through the hashmap once as well.
        # the most straighforward solution is to simply loop through the string and record all the dna sequences I come across as I loop through the input. 
        # whenever I come across a string that is already in the hashmap than I add the sequence to the outgoing array.

        # hashMap = {"dna sequence: [number of instances]"}

        hash_map = {}
        results = []

        if len(s) >= 10:
            for i in range(len(s)-10 + 1):
                currentSequence = s[i:i+10]
                if currentSequence in hash_map:
                    hash_map[currentSequence] += 1
                else:
                    hash_map[currentSequence] = 1

            for sequence, count in hash_map.items():
                if count > 1:
                    results.append(sequence)

        return results