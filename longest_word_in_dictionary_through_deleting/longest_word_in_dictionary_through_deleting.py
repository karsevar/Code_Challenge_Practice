class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # first we will need to create a solutions array that will contain all the words that fit into the input string.
        # create a for loop that will iterate through the dictionary array
        # create a string pointer (that will keep track of the index position in the string)
        # create a word pointer (that will keep track of the index position in the word)

        # create a while loop that will iterate through the both the word and the string 
        # the while loop will terminate once the string_index pointer reaches the end of the string

        # conditional if string_pointer equals word_pointer iterate both string_pointer and word_pointer
        # conditional if string_pointer does not equal word_pointer iterate string_pointer

        # conditional if string_pointer equals word_pointer and word_pointer is equal to len(word[i]) - 1 
        # add word to the solutions array.

        # create a for loop through solutions array and find the longest word (will need to fix this part later)

        # the time complexity for this solution is O(n*m) since we are interating through first the dictionary and then the string

        matching_words = []

        for word in dictionary:
            string_pointer = 0 
            word_pointer = 0

            while string_pointer < len(s):
                if word_pointer >= len(word):
                    break

                if word[word_pointer] == s[string_pointer]:
                    if word_pointer == len(word) - 1:
                        matching_words.append(word) 
                        break
                    word_pointer += 1
                    string_pointer += 1
                else:
                    string_pointer += 1

        print(matching_words)
        if len(matching_words) == 0:
            return ""
        matching_words.sort()
        longest_word = matching_words[0]
        for word in matching_words:
            print("longest word: ", longest_word)
            if len(longest_word) < len(word):
                longest_word = word
            elif len(longest_word) == len(word):
                if longest_word > word:
                    longest_word = word

        return longest_word