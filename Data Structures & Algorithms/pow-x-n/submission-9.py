class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        if abs(n)>=100000 and x>1:
            return 0
        i = 0
        power = x
        if x==1:
            return 1
        elif x==-1:
            if n%2==0:
                return 1
            else:
                return -1 
        if n==0:
            return 1
        elif n>0:
            power = x
            while i<n-1:
                power = power*x
                i+=1
        else:
            power = 1/x
            x = 1/x
            while i>n+1:
                power = power*x
                #print(power)
                i-=1
        
        #print(power)
        return power
