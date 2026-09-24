class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # to simulate this problem we will need to iterate over and shrink the array until there is only one stone left in the array.

        # will need to create a while loop that will terminate when the size of the array reaches 1 or below.

        # we need to collect the largest two values in the array and use the predefined rules to destroy both of them if they are equal, return y - x in the i index place if they are not equal.

        while len(stones) > 1:
            stones.sort(reverse=True)

            if stones[0] != stones[1]:
                new_stone = stones[0] - stones[1]
                stones.pop(1)
                stones[0] = new_stone
            elif stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)

        return stones[0] if len(stones) == 1 else 0