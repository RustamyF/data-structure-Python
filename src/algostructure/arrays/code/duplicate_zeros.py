"""
              Duplicate Zeros
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Test case 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

test case 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]


Solution:
The problem is asking us to duplicate zero elements in the array when we enounter them. We do not have to increase
the length of the array. We can do that by looping over every element of the array and every time we encounter a zero
element, we first shift all the elements to the right of zero by one then add a zero.
"""


class Solution:
    def duplicate_zeros(self, nums):
        i = 0
        # loop over every element in the array
        while i < len(nums) - 1:
            # if the element is zero, shift all the element to the right by one.
            if nums[i] == 0:
                # shift all the element to the right by one
                for j in reversed(range(i, len(nums) - 1)):
                    nums[j + 1] = nums[j]
                # now that everything to the right is shifted, add a zero
                nums[i + 1] = 0
                # increase the step by one
                i += 1
            i += 1
        return nums

