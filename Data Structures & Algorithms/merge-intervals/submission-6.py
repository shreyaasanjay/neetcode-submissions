class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        #print(intervals)
        result = []

        
        i=0
        while i<len(intervals)-1:
            #print(i, intervals[i], intervals[i+1])
            if intervals[i][0]==intervals[i+1][0]:
                intervals[i] = [intervals[i][0],max(intervals[i][1], intervals[i+1][1])]
                del intervals [i+1]
                
            elif intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                del intervals [i+1]
            else:   
                i+=1
        #print(intervals)
        return intervals
