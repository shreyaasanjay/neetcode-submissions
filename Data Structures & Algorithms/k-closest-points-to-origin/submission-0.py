class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = 0
        distances = []
        result = []
        

        #get distance from origin
        for i in points:
            distance = math.sqrt(i[0]*i[0] + i[1]*i[1])
            distances.append((distance, i))
            
        heapq.heapify(distances)
        print(distances)
        
        i=0
        while i<k:
            result.append(heapq.heappop(distances)[1])
            i+=1

        return result


        