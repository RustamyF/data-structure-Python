"""3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""


class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        length = len(nums)
        for i in range(length - 1):
            left = i + 1
            right = length - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[right], nums[left]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result
nums = [-1,0,1,2,-1,-4]
my_result=Solution()
print(my_result.threeSum(nums))


nums = []
print(my_result.threeSum(nums))

nums = [0]
print(my_result.threeSum(nums))

nums=[0,0,0,0]
print(my_result.threeSum(nums))

nums=[-2,0,0,2,2]
print(my_result.threeSum(nums))
