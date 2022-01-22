"""Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
class Solution:
    def productExceptSelf(self, nums):
        length=len(nums)
        left=[0]*length
        right=[0]*length
        left[0]=1
        right[-1]=1
        for i in range(1, length):
            left[i]=left[i-1]*nums[i-1]
        for i in reversed(range(length-1)):
            right[i]=right[i+1]*nums[i+1]
        result=[]
        for i in range(length):
            result.append(left[i]*right[i])
        return result

nums = [1,2,3,4]
result=Solution()
print(result.productExceptSelf(nums))

nums = [-1,1,0,-3,3]
result=Solution()
print(result.productExceptSelf(nums))

