"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of
intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""

class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        result=[]
        count=0
        result.append(intervals[0])
        for index, interval in enumerate(intervals[1:]):
            int1=result[-1]
            if interval[0]>=int1[1]:
                result.append(interval)
            else:
                if int1[1]>interval[1]:
                    result[-1]=interval
                count+=1
        return count, result



intervals = [[1,2],[2,3],[3,4],[1,3]]
my_result=Solution()
print(my_result.eraseOverlapIntervals(intervals))

intervals = [[1,2],[1,2],[1,2]]
print(my_result.eraseOverlapIntervals(intervals))

intervals = [[1,2],[2,3]]
print(my_result.eraseOverlapIntervals(intervals))

intervals=[[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
print(my_result.eraseOverlapIntervals(intervals))