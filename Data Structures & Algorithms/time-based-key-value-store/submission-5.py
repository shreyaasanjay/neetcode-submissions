class TimeMap:

    def __init__(self):
        self.keyvaluetime = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #hashmap with value as the key and then an array with key and value as the value
        
            if key not in self.keyvaluetime:
                self.keyvaluetime[key] = [[value,timestamp]]
            else:
                self.keyvaluetime[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        #print(self.keyvaluetime)
        
        if key not in self.keyvaluetime:
            return ""
        left = 0
        right = len(self.keyvaluetime[key])
        mid = 0
        if key in self.keyvaluetime:
            while left<right:
                mid = (left+right)//2
                if self.keyvaluetime[key][mid][1]==timestamp:
                    return self.keyvaluetime[key][mid][0]
                elif self.keyvaluetime[key][mid][1]<timestamp:
                    left=mid+1
                else:
                    right=mid
            if left==0:
                    return ""
                
            return self.keyvaluetime[key][left-1][0]
                


        

        

