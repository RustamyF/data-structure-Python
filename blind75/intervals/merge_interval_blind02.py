"""Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution:
    def merge(self, intervals):
        intervals.sort()
        result=[]
        result.append(intervals[0])
        for index, interval in enumerate(intervals[1:]):
            int1=result[-1]
            int2=interval
            if int2[0]>int1[1]:
                result.append(int2)
            else:
                newInt=[min(int1[0], int2[0]), max(int1[1], int2[1])]
                result[-1]=newInt
        return result

my_result=Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(my_result.merge(intervals))

intervals = [[1,4],[4,5]]
print(my_result.merge(intervals))