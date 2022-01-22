"""Maximum Product Subarray
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct_bruteForce(self, nums) -> int:
        lenth=len(nums)
        maxMax=0
        for i in range(lenth):
            curMax = nums[i]
            for j in range(i+1,lenth):
                curMax=max(nums[j], curMax*nums[j])
                maxMax=max(curMax,maxMax)
        return maxMax
    def maxProduct(self, nums) -> int:
        if len(nums)==0:
            return 0
        curMax=1
        curMin=1
        result=max(nums)

        for cur in nums:
            temp_max=max(cur, cur*curMax, cur*curMin)
            curMin=min(cur, cur*curMax, cur*curMin)
            curMax=temp_max

            result=max(result,curMax)
        return result

nums = [2, 3, -2, 4]
result=Solution()
print(result.maxProduct_bruteForce(nums))
print(result.maxProduct(nums))


nums = [-2,0,-1]
result=Solution()
print(result.maxProduct_bruteForce(nums))
print(result.maxProduct(nums))
