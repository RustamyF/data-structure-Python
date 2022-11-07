""""              Max Consecutive Ones
Problem statement
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Test case 1
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Test case 2
Input: nums = [1,0,1,1,0,1]
Output: 2

##### Solution
We can solve this problem by passing through every element in the array and keeping track of the
maximum number of consecutive ones. The following sinpit shows the python solution.
"""""


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        curmax, maximum = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curmax += 1
            else:
                curmax = 0
            maximum = max(maximum, curmax)
        return maximum
