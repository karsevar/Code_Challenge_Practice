class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # according to dynamic window principles all I need to do is move the right pointer until the flip counter reaches k and then move the left pointer within a while loop that will terminate once nums[left_pointer] reaches k 0s in the array.
        # effectively counting happens with the right pointer while the left pointer is used to close the window and make the flip counter go back to zero 

        # create a maximum substring variable
        # create a left pointer variable that will keep track of the beginning of the subarray
        # create a flip counter initialize the variable to zero 
        # create current_counter variable

        # create a for loop that will be used as the right pointer
        # check if nums[right_pointer] is 1 
        # if it is than iterate current_counter by one
        # if nums[right_pointer] is 0 
        # check if flip_counter is less than k
        # if so iterate flip_counter by one and current_counter by one
        # if false 
        # create a while loop that will terminate once left_pointer is equal to right_pointer
        # check if nums[left_pointer] is equal to one 
        # if true decrement current_counter by one 
        # if false decrement current_counter and flip_counter by one
        # break from loop when flip_counter is equal to zero

        maximum_substring = 0
        left_pointer = 0 
        flip_counter = 0 
        current_counter = 0

        for right_pointer in range(len(nums)):
            print("counter: ", current_counter, "flip_counter: ", flip_counter)
            if nums[right_pointer] == 1:
                current_counter += 1
            else:
                flip_counter += 1
                if flip_counter > k:
                    if maximum_substring < current_counter:
                        maximum_substring = current_counter
                    while flip_counter > k:
                        if nums[left_pointer] == 1:
                            left_pointer += 1
                            current_counter -= 1
                        else:
                            flip_counter -= 1
                            left_pointer += 1
                            current_counter -= 1
                current_counter += 1

        if current_counter > maximum_substring:
            maximum_substring = current_counter

        return maximum_substring
    

# simplified logic with the same sliding window principles except I used a queue to keep track of the 
# left pointer. 
class SolutionQueue:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # the most straightforward way to solve this is to have two specific counters: one for counting the current consecutive ones for each iteration, another counter for keeping track of the number of zeros that were converted to ones (this will be the shrinking criterion) 
        # also perhaps adding a pointer for the left part of the subarray might be a good idea as well. 

        # also I think that perhaps using a queue might be a better idea than using a left pointer as I can shrink the queue and add to it according to the expand and shrink criterion.

        # create a convert zero to one counter this will be initialized to 0 
        # create a maximum length variable initialize it to zero 

        # create a for loop that will start at index zero and end at the end of the input nums array.
        # check if current index is a one
        # if true add index to queue array 
        # if false check 
        # increment zero counter by one and add the index to queue array 
        # if zero counter is greater than k 
        # shrink the queue through a while loop until zero counter is less than k
        # check if removed element is a zero if so decriment zero counter

        maximum_length = 0
        zero_counter = 0
        queue = []

        for i in range(len(nums)):
            if nums[i] == 1:
                queue.append(nums[i])
            else:
                queue.append(nums[i])
                zero_counter += 1

                while zero_counter > k:
                    head_value = queue.pop(0)
                    if head_value == 0:
                        zero_counter -= 1

            if maximum_length < len(queue):
                maximum_length = len(queue)

        return max(maximum_length, len(queue))

        
        