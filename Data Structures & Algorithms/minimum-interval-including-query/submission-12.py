class Solution:
    import copy
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #we sort by height so the first thing that satisifes the query is returned, ig we make a hashmap of the interval and its height and we sort the hashmp by the index and then iterate over the values
#NEVERMIND this doesnt work because we cant make the keys of a hashmap a list bc its mutable so we'll have to use the heap thing --> we sort the intervals by thir start value ohh and for each query, we add intervals to the min heap that fit the query and we ohh because 
        import copy
        heap = []
        result = [0] * len(queries)
        intervals.sort()
        query = []
        for i in range(len(queries)):
            query.append((queries[i],i))
        #print(query)
        heappointer = 0


        for i in sorted(query):
            while heappointer<len(intervals) and intervals[heappointer][0]<=i[0]:
                heapq.heappush(heap, (intervals[heappointer][1]-intervals[heappointer][0] + 1, intervals[heappointer][1]))
                heappointer+=1
            #print(i, heap)
            #heapq.heapify(heap) - heappush already heapifies
            
            while len(heap)>0 and heap[0][1]<i[0]:
                    heapq.heappop(heap)
            #print("after popping")
            #print(i, heap)
            if heap:
                
                result[i[1]]= heap[0][0]
                #print(result)
            else:
                result[i[1]]=-1
        return result

        