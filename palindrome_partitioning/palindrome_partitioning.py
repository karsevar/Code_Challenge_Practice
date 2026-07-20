# Time complexity is O(n * 2^n) 2^n for all the partitions and O(n) for the palindrome checks and substring creation
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        print("string: ", s)
        self.n = len(s)

        # This is an interesting problem.
        # so for this problem I'm given the recursion function with all the required arguments. It seems that I will be able to modify the partition_recursion function to better suit my needs if on the off chance that I need to include index and a visited set.

        # it seems that the main idea is to loop through the string and create palindrome partition permutations. A possible idea is to loop through each individual letter in the string (s). create a conditional that will check if the reverse of the current partition is equal to itself if so than we can add it to the current_partition list.
        string_partitions = []

        self.partition_recursion(s, 0, [], string_partitions)

        return string_partitions

    def partition_recursion(self, s: str, index: int, current_partition: List[str], string_partitions: List[List[str]]):
        if index == self.n:
            string_partitions.append(current_partition[:])
            return 

        for i in range(index, len(s)):
            if self.is_palindrome(s[index:i+1]):
                current_partition.append(s[index:i+1])
                self.partition_recursion(s, i+1, current_partition, string_partitions)
                current_partition.pop()

    def is_palindrome(self, s):
        return s == "".join(reversed(s))