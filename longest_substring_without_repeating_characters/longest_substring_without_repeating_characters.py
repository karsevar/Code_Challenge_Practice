class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # so in other words this is a two pointer problem and I'm just supposed to keep a tally of the length of the substring. The main question is if I reach a value that is a repeat character do I reset to the tally to zero? Will need to experiment a little more with this problem.

        left = 0
        max_subset = 1 
        current_subset = 1

        if len(s) == 0:
            return 0
        character_set = set(s[0])

        for right in range(1, len(s)):

            if s[right] not in character_set:
                current_subset += 1
                character_set.add(s[right])
            else:
                while s[right] in character_set:
                    if left == right:
                        break
                    if left == len(s) - 1:
                        break
                    current_subset -= 1
                    character_set.remove(s[left])
                    left += 1
                character_set.add(s[right])

            max_subset = max(max_subset, right - left + 1)

        return max_subset