"""Search in Rotated Sorted Array
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


class Solution:
    def search(self, nums, target: int) -> int:

        def find_minIndex(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

        def bst(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        index = find_minIndex(nums)
        leftside = bst(nums[:index], target)
        rightside = bst(nums[index:], target)
        if rightside is not False:
            return rightside + index
        if leftside is not False:
            return leftside
        return -1

my_result=Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(my_result.search(nums,target))

nums = [4,5,6,7,0,1,2]
target = 3
print(my_result.search(nums,target))


nums = [1]
target = 0
print(my_result.search(nums,target))
