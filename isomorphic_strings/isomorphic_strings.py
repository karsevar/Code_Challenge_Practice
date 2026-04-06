class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # I believe that the rules for a word being isomorphic is that they both need to be of similar length and that each individual characters will need to map between both s and t with no overlap

        # first create an edge case if statement that catches if the two strings don't have identical lengths.
        # initialize a map that will keep track of the s[i] -> t[i] letter dissigations.
        # create a while loop that will loop through both strings s and t using the same index value i. 
            # if s[i] is not found in variable map then add s[i] and t[i] to the map.
            # if s[i] is found in the map check if t[i] the same as the assigned value in the map.
            # if the above condition comes back false then return false

        # return true as the default

        if len(s) != len(t):
            return False

        s_letter_map = {}
        t_letter_map = {}
        i = 0

        while i < len(s):
            if s[i] in s_letter_map:
                if s_letter_map[s[i]] != t[i]:
                    return False
            if t[i] in t_letter_map:
                if t_letter_map[t[i]] != s[i]:
                    return False
            if t[i] not in t_letter_map and s[i] not in s_letter_map:
                s_letter_map[s[i]] = t[i]
                t_letter_map[t[i]] = s[i]
            i += 1

        return True