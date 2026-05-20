class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # this is my first attempt for this problem the time complexity is O(n^2) since I'm going through the s string twice through 
        # two nested for loops.

        # A possible solution for this is to again have a nested for loop that will keep track of two pointers the i pointer will keep track of the beginning of the substring and j will keep track of the end of the substring. We can have counters for the amount of characters the substring has and a character flip counter that will decriment if the character does not line up with s[i].

        # create a maximum_substring variable

        # create a for loop that will keep track of the beginning of the substring as index i
        # create a substring counter and increment it by one
        # create a for loop that will keep track of the ending of the substring as index j
        # check if s[j] is the same as s[i] 
        # if not check if flip counter is not zero
            # if it is not zero decriment the counter by one
            # if it is zero break the inner loop and reset flip counter 
        # if they are the same increment current_substring counter

        # interesting the main breaking point in my logic is choosing between which character to pick as the correct conditional for the repeat character. In this case it fails at ABBB where I should pick B in place of A. This iteration works for some of the test cases but not all of them.
        # will need to come back to this question

        maximum_substring = 0

        for i in range(len(s) - 1):
            current_substring = 1
            flip_counter = k
            for j in range(i + 1, len(s)):
                if s[i] != s[j]:
                    if flip_counter != 0:
                        flip_counter -= 1
                        current_substring += 1
                    else:
                        if maximum_substring < current_substring:
                            maximum_substring = current_substring
                        break
                else:
                    current_substring += 1

            if current_substring > maximum_substring:
                maximum_substring = current_substring

        return maximum_substring