class Solution:
    # first attempt at this problem. It is only passing 18 out of 40 test cases. 
    # This solution can be regarded as a brute force solution with a combination of sliding window.
    # I'm looping through the input array initially one time to get the sequences and than I'm looping through 
    # the input array again for n number of subsequences.
    # The time complexity of this solution is O(n^2) and the space complexity is O(n).
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # the bruteforce method is to simply create a list of letter sequences that satisfy the maxLetters, minSize and maxSize requirements.

        # then loop through the array again to find which sequence has the highest amount occurances. 

        # create a repeat letter counter
        # inplace of creating a set that will keep track of the occurances of letters I think the best idea is to use a queue to keep track of the current subarray. This sub array will expand and contract according to the the conditionals on max and min size and max letters.

        # create a for loop that will keep track of the right pointer. The beginning of the queue will act as the left pointer value. 

        # check if queue is greater than or equal to minSize, less than or equal to maxsize, and has equal to or less letters than max letters
        # if true add a new letter to queue 
        # if new letter is not in queue increment letter counter by one
        # create a while loop that will end when the length of queue is less than maxSize, greater than minsize, and has less than or equal to letters as maxLetters
            # in the loop pop first letter from the queue check if the queue has an additional letter of the one removed
            # if false decriment letterCounter

        # create a conditional that adds the substring to a dictionary that will retain a count of all possible substrings in the input string.

        # lastly create a for loop that will loop through the hashmap and return a substring with the largest amount of occurances.

        letterCounter = 0
        subSequences = set() # {"subarray": [amount of occurances]}
        queue = []

        for right_pointer in range(len(s)):
            # print("queue: ", queue, " right pointer: ", s[right_pointer])

            if s[right_pointer] not in queue:
                letterCounter += 1
            queue.append(s[right_pointer])

            while maxSize < len(queue) and maxLetters < letterCounter:
                letter = queue.pop(0)
                # print("pop letter: ", letter)
                if letter not in queue:
                    letterCounter -= 1

            # print("while loop queue: ", queue, " right pointer: ", s[right_pointer])

            if minSize <= len(queue):
                subSequences.add("".join(queue))


        print("sequence: ", subSequences)

        maxCount = 0

        for sequence in subSequences:
            currentCount = 0
            for i in range(len(s) - len(sequence) + 1):
                if sequence == s[i:i+len(sequence)]:
                    currentCount += 1

            if maxCount < currentCount:
                maxCount = currentCount

        return maxCount

    # Modified my solution with an editorial found online though ignoring maxSize doesn't seem like a good strategy 
    # as well. This passes all test cases but I might need to find a better solution that is less hacky.
    def maxFreqSolution(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        letterCounter = 0
        subSequences = {} # {"subarray": [amount of occurances]}
        queue = []
        maxCount = 0

        for right_pointer in range(len(s)):
            # print("queue: ", queue, " right pointer: ", s[right_pointer])

            if s[right_pointer] not in queue:
                letterCounter += 1
            queue.append(s[right_pointer])

            while maxLetters < letterCounter or minSize < len(queue):
                letter = queue.pop(0)
                # print("pop letter: ", letter)
                if letter not in queue:
                    letterCounter -= 1

            # print("while loop queue: ", queue, " right pointer: ", s[right_pointer])

            if minSize == len(queue):
                curr = "".join(queue) 
                subSequences[curr] = subSequences.get(curr, 0) + 1

                maxCount = max(maxCount, subSequences[curr])

        return maxCount