class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # This is a fixed sliding window problem because I'm attempting to fit p into s. In other words, I'm finding how many anagrams that are in s for the characters in p. The length of the window will be the length of the p string.

        # convert s and p into arrays for easier data handling and for easier character lookup between the two strings.
        # One thing to keep in mind that we will need to think about alphabetic order sorting between the p string and the window string within the s string since the problem is asking for if the window has the same characters as p.


        # first convert s and p into lists.
        # sort p by alphabetical order.
        # get the length of p 
        # get the length of s

        # initialize a list that will carry the first indexes the anagram starts

        # Initialize the first window p[:length_p]
        # if first window is an anagram sort(p[:length_p]) == s 
        # anagram_indexes.append(0)

        # create a for loop that will start at index 1 and end at length_s - length_p
        # use the same steps as above within the loop

        # return anagram_indexes

        # Issues to consider with this implementation:
        ## This is not a completely efficient implementation of the sliding window algorithm since I'm not reusing the s string window as something like a queue where I can use the partial computations from the previous window to decrease the amount of computations needed to calculate the current window. Will need to think about this issue when fixing this solution

        s_array = list(s)
        p_array = list(p)
        p_array = sorted(p_array)

        s_length = len(s_array)
        p_length = len(p_array)

        if s_length == 0:
            return []
        if s_length < p_length:
            return []

        anagram_indexes = []

        for i in range(s_length - p_length + 1):
            if p_array == sorted(s_array[i:i+p_length]):
                anagram_indexes.append(i)

        return anagram_indexes