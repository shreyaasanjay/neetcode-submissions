class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #brute force is to go through and find every pair where the interval is overlapping and if there are similarities, then delete that value?
        #greedy approach - we first start at the frist interval and we keep the prev interval end stored, once we find an interval that makes it invalid (start is less than previous interval), we add one to result and move on without updating

        intervals.sort()
        print(intervals)
        result = 0
        prevend = intervals[0][1]

        i=0

        for i in range(1, len(intervals)):
            if intervals[i][0]<prevend:
                prevend = min(prevend, intervals[i][1])
                result+=1
            else:
                prevend = intervals[i][1]
        
        return result
