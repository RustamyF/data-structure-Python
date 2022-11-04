""" Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
from typing import List


class Solution:
    def __init__(self):
        self.index = None

    def search(self, nums: List[int], target: int) -> int:
        """
        :param nums: list of numbers
        :param target: target value
        :return: index of the target
        """

        def find_min_index(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

        self.index = find_min_index(nums)

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                else:
                    if target > arr[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
            return -1

        # if target is the smallest element
        if nums[self.index] == target:
            return self.index
        # if array is not rotated, search in the entire array
        if self.index == 0:
            return binary_search(nums, target)
        if target < nums[0]:
            return binary_search(nums[self.index:], target)
        return binary_search(nums[:self.index], target)