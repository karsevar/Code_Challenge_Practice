class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # create a main_pointer that will keep track of the unique numbers in the array 
        # create a duplicate_pointer that will iterate through the array if a value is found that is the same as the main pointer

        # create a while loop that will terminate when the duplicate_pointer or the main_pointer reaches the end of the array

        # conditional if the duplicate_pointer is the same as the main_pointer value iterate duplicate_pointer by one
        # conditional if the duplicate_pointer is not the same as the main_pointer move main_pointer by one and set nums[duplicate_pointer] as nums[main_pointer + 1]

        # time complexity for this solution will be O(n) since it is only iterating through the array once in the worst case where the values are all unique.


        if len(nums) <= 1:
            return len(nums)

        main_pointer = 0
        duplicate_pointer = 1

        while duplicate_pointer < len(nums):
            # print("main_pointer: ", main_pointer, " duplicate_pointer: ", duplicate_pointer)
            if duplicate_pointer > len(nums) or main_pointer > len(nums):
                break
            if nums[duplicate_pointer] == nums[main_pointer]:
                nums[duplicate_pointer] = "_"
                duplicate_pointer += 1
            else:
                main_pointer += 1
                nums[main_pointer] = nums[duplicate_pointer]
                duplicate_pointer += 1

        # print("nums: ", nums)

        return main_pointer + 1
        
        