class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #basic idea:
        # we first sort the cars by position so our first car has the greatest position
        #meaning it will always be at the front of the car fleet 
        #we add the first car to the stack, and calculate its time - if the next car is going to pass it 
        #we pop the next car and add it to our fleet, if not, we append to our stack

        fleetsize = 1
        lane = []
        maxtime = 0
        time = 0.0

        speedpos = []

        for i in range(len(position)):
            speedpos.append((position[i],speed[i]))

        speedpos.sort()
        speedpos = speedpos[::-1]
        

        for i in speedpos:
            if len(lane)>0:
                lane.append(i)
                time = (target - i[0])/i[1]
                if time<=maxtime:
                    lane.pop()
                else:
                    fleetsize +=1 
                    maxtime = time
                    
            else:
                lane.append(i)
                maxtime = (target - i[0])/i[1]
    
        return fleetsize

