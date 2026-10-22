"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #this is the step function algo
        #make events for start and stop and with start

        events = []
        start_event = ()
        stop_event = ()

        if len(intervals)==0:
            return 0

        for i in intervals:
            start_event=(i.start, 1)
            stop_event=(i.end, -1)
            events.append(start_event)
            events.append(stop_event)

        events.sort()
        #print(events)

        max_rooms = 1
        running_rooms=0
        for i in events:
            running_rooms+=i[1]
            if running_rooms>max_rooms:
                max_rooms = running_rooms

        return max_rooms