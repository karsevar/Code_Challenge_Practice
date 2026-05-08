class Solution:
    def merge(self, nums1, m, nums2, n):
        # I believe that the best solution might be to have two pointers. One that starts at the beginning of nums2 and the second that starts at the end of nums1.

        # The main thing to consider is the conditional that comparse nums1[pointer] with nums2[pointer]

        # first attempt it seems that I was not considering the fact that there might be 0's in nums1 that are not part of the sorted array. I need to make sure that I am not comparing those 0's with the values in nums2.
        
        for nums2_pointer in range(len(nums2)):
            print("nums2_pointer: ", nums2[nums2_pointer])
            nums1_pointer = len(nums1) - 2
            while True:
                print("nums1 array: ", nums1)
                if nums1[nums1_pointer] == 0 and nums1_pointer != 0:
                    nums1_pointer -= 1
                elif nums1[nums1_pointer] == 0 and nums1_pointer == 0:
                    nums1[nums1_pointer] = nums2[nums2_pointer]
                else:
                    if nums1[nums1_pointer] <= nums2[nums2_pointer]:
                        if nums1_pointer == 0 and nums1[nums1_pointer] == 0: 
                            nums1[nums1_pointer] = nums2[nums2_pointer]
                            break
                        else:
                            nums1[nums1_pointer + 1] = nums2[nums2_pointer]
                            break
                    else:
                        nums1[nums1_pointer + 1] = nums1[nums1_pointer]
                        nums1[nums1_pointer] = 0

                if nums1_pointer < 0:
                    break

            if len(nums1) == 1:
                nums1[0] = nums2[nums2_pointer]