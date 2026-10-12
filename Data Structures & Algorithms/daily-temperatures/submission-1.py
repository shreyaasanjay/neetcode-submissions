class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #using a stack yuh

        temps = []
        indices = [0] * len(temperatures)
        index = 0
        previndices = []

        #enumerate!! j is the curerent index and i is the current temperature value
        for j,i in enumerate(temperatures):
            if len(temps)>0:
                if temps[-1] >= i:
                    temps.append(i)
                    previndices.append(j)
                    #print(temps)
                else:
                    #print(temps)
                    while len(temps)>0 and len(previndices)>0 and temps[-1]<i:
                        index=j-previndices[-1]
                        indices[previndices.pop()] = index
                        #temperatures.remove(temps[-1])
                        #print(indices)
                        temps.pop()
                    temps.append(i)
                    previndices.append(j)
                    #print(temps)
            else:
                temps.append(i)
                previndices.append(j)
        #print(indices)

        return indices