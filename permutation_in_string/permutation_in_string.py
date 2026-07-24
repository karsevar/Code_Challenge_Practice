class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # this seems straight forward since all I need to assess is if s1 is in s2 and the length of the window is dictated by the length of s1.

        # first check if s1 is greater in length than s2 if so then the answer is clearly false

        # sort s1 to make finding permutations easier within s2

        # create for loop that will start at zero index and end at len(s2) - len(s1) + 1
        # check if sorted(s2[i:i+len(s1)]) is equal to s1
        # if true return true

        # return false

        s1_array = sorted(s1)

        if len(s1) > len(s2):
            return False

        for i in range(len(s2) - len(s1) + 1):
            if sorted(s2[i:i+len(s1)]) == s1_array:
                return True

        return False