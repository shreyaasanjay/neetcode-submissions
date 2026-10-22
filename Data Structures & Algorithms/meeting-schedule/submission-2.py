"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        #intervals.start.sort()
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                print(intervals[i].end, intervals[j].start)
                if intervals[i].end > intervals[j].start:
                    if intervals[i].start<intervals[j].end:
                        return False
        return True
