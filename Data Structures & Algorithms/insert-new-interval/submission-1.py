class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #two parts to this
        #one - insert the array int he intervals
        #merge all intervials

        #insert
        i=0
        intervals.append(newInterval)
        intervals.sort()
        
        #print(intervals)

        #merge
        i=0
        while i<len(intervals)-1:
            if intervals[i+1][0]<=intervals[i][1]:
                intervals[i]=[intervals[i][0], max(intervals[i][1],intervals[i+1][1])]
                del intervals[i+1]
            else:
                i+=1
            
        
        #print(intervals)

        return intervals
