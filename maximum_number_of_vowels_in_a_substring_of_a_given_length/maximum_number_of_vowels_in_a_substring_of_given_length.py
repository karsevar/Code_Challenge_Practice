class Solution:
    # fixed window solution
    def maxVowels(self, s: str, k: int) -> int:
        # This actually looks like a fixed length window problems since they gave use the size of the window (substring) that we need to process. Which means that the sequence of vowels will never be larger than k. 

        # First course of action is to calculate the initial values.
        # set vowel count to 0 
        # set maximum vowel count to 0

        # calculate the origin window and the initial vowel count and maximum vowel count.

        vowels = set([
            'a',
            'e',
            'i',
            'o',
            'u'
        ])

        vowel_count = 0
        maximum_vowels = 0

        for char in s[:k]:
            if char in vowels:
                vowel_count += 1

        maximum_vowels = vowel_count

        for i in range(len(s) - k):
            if s[i] in vowels:
                vowel_count -= 1
            
            if s[i+k] in vowels:
                vowel_count += 1

            if vowel_count > maximum_vowels:
                maximum_vowels = vowel_count

        return maximum_vowels