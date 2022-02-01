"""Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


class Solution:
    def canJump(self, nums) -> bool:
        # start with a jump length of one
        count = 1
        # loop over reversed of the list
        for i in reversed(range(1,len(nums))):
            # if the number before the goal was smaller than the jump, increase the jump by one
            if nums[i-1]<count:
                count+=1
            # if the number before the goal was larger or equal to the jump, bring the jump space to one
            else:
                count=1
        # if count was one, it means that there was a jump to the end
        return count==1


my_result=Solution()
nums = [3,2,1,0,4]
print(my_result.canJump(nums))

nums = [3,3,0,0,4]
print(my_result.canJump(nums))

nums = [2,3,1,1,4]
print(my_result.canJump(nums))

nums = [2,0]
print(my_result.canJump(nums))
nums = [0]
print(my_result.canJump(nums))