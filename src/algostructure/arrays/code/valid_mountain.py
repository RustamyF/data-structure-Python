"""         Valid Mountain Array
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

##### Solution
We can use two pointers for this problem one starting from left and one from right. We loop over the entire array
and increase the left index when arr[left+1]>index[left] and decrease the right index by one when arr[right-1]>index[right].
At the end when left is equal to right and both are not zero, it is a valid mountain array. We do not want
either left or right to be zero at the end because it means that the values did not increase.
"""


class Solution:
    def validMountainArray(self, arr) -> bool:
        # start a left pointer and a right pointer
        left, right = 0, len(arr) - 1
        # loop over each element in the array
        for i in range(len(arr)):
            # if the array is increasing from left, increase the left by one
            if arr[left + 1] > arr[left]:
                left += 1
            # if the array is increasing from right, decrease the right by one
            if arr[right - 1] > arr[right]:
                right -= 1
        # if left and right are the same and are not zero, it is a valid mountain
        return left == right and not (left == 0 or right == 0)