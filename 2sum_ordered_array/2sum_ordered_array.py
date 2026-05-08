class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # easiest solution is to simply using the bruteforce method by simply using a nested for loop that will iterate through the numbers array using two pointers 

        # create an initial for loop that will keep track of index i and end at len(numbers) - 2 index
        # create another for loop that will keep track of index j and end at the end of the numbers array len(numbers) - 1
        # create a conditional that will check if numbers[i] + numbers[j] == target
        # if true return the indexes in an array

        # if no matches are found return an empty array

        # Simpliest solution but the time complexity can be interpreted as O(n^2) since we are looping through the array twice within a nested for loop.

        # for i in range(len(numbers) - 1):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return []


        # Two pointer solution:
        # According to the literature we can use the two pointer technique through starting a pointer at the beginning of the array and one at the end of the array.
        # conditionals for moving either the left or right pointer
        ## if the sum is greater than the target we will need to move the right pointer down one
        ## if the sum is less than the target we will need to move the left pointer up one
        ## if the sum is equal to the target than we return the index positions

        # create a conditional that will return an empty array if the length of the array is less than 2

        # initialize a right pointer and set it to the beginning of the array
        # initialize a left pointer and set it to the end of the array

        # create a while loop that will terminate once right and left pointers collide 
        # calculate the sum value between the two pointers
        # if sum value is equal to target return the array of the index positions
        # if sum value is less than target move left pointer by one
        # if sum value is greater than target move right pointer down one

        # time complexity for this can be calculated in the worst case as O(n) since it seems that I'm only looping through the numbers array once.

        left_pointer = 0
        right_pointer = len(numbers) - 1

        while True:
            if left_pointer == right_pointer:
                break
            
            sum_value = numbers[left_pointer] + numbers[right_pointer]
            if sum_value == target:
                return [left_pointer + 1, right_pointer + 1]
            elif sum_value > target:
                right_pointer -= 1
            elif target > sum_value:
                left_pointer += 1

        return []