"""Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""
class Solution:
    def minMeetingRooms(self, intervals):
        start=sorted([i[0] for i in intervals])
        end=sorted([i[1] for i in intervals])

        s,e=0,0
        res,count=0,0
        while s<len(intervals):
            if start[s]<end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res=max(count,res)
            print(s,e)
        return res

intervals = [[0,30],[5,10],[15,20]]

my_result=Solution()
print(my_result.minMeetingRooms(intervals))
intervals = [[7,10],[2,4]]
print(my_result.minMeetingRooms(intervals))

intervals = [[0,6],[0,7],[5,6]]
print(my_result.minMeetingRooms(intervals))
