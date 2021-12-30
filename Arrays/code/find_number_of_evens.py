"""
              Find Numbers with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.

Test case 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.

test case 2:
Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.


Solution:
The problem is asking us to find the number of digits that have even number of digits. For example 23 has two digits
and 345 has three digits. We can solve this problem by converting each number in the array to a string and find the length
of that string and divide it by two. If there is nor reminder, we count that as an even number of digits.
"""
class Solution:
    def findNumbers(self, nums):
        # Start the counter from zero
        count=0
        # loop over each element in the bytearray
        for num in nums:
            # convert the number to a string and divid its length to 2.
            if len(str(num))%2==0:
                # if the remainder is equal to zero, increase the counter by one.
                count+=1
        return count
result=Solution()

# test 1
array=[12,345,2,6,7896]
print(result.findNumbers(array))

# test 2
array=[555,901,482,1771]
print(result.findNumbers(array))
