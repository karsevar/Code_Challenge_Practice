class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the smartest way to solve this is to look through strs in a single for loop and for each word in the strings input we need to order them.

        # hashmap = {[ordered letters: [strs[word], strs[word]]]}

        # Time complexity can be interpreted as O(n * l) where n is the length of the input strs array and l is the length of each individual word in the array. 
        # space complexity can be interpreted as O(n) in the worst case where each word in the input strs array has its own key and value pair

        word_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]

        return list(word_map.values())