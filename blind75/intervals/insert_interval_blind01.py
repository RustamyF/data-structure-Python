"""Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
class Solution:
    def insert(self, intervals, newInterval):
        result=[]
        for i, interval in enumerate(intervals):
            if newInterval[1]<interval[0]:
                result.append(newInterval)
                return result+intervals[i:]
            elif newInterval[0]>interval[1]:
                result.append(interval)
            else:
                newInterval=[min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        result.append(newInterval)
        return result




intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

my_result=Solution()
print(my_result.insert(intervals, newInterval))

intervals=[[1,3],[6,9]]
newInterval = [2,5]
my_result=Solution()
print(my_result.insert(intervals, newInterval))