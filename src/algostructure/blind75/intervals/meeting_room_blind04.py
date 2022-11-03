"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
"""

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort()
        length = len(intervals)
        for i in range(length - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


intervals = [[0,30],[5,10],[15,20]]
my_result=Solution()
print(my_result.canAttendMeetings(intervals))

intervals = [[7,10],[2,4]]
print(my_result.canAttendMeetings(intervals))
