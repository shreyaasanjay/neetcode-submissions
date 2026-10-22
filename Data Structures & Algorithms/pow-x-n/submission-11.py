class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #recursive solution
        print(n)

        if n>=100000 and x>1:
            return 0
        print("prerecursion")
        if x==0:
            return 0
        
        elif n==0:
            return 1
        
        else:
            res = self.myPow(x, abs(n)//2) ** 2
        
        print(res)
        print("post recursion")

        if n<0 and res!=0:
            if n%2==1:
                return 1/res * 1/x
            else:
                return 1/res
        else:
            if n%2==1:
                return res * x
            else:
                return res
         

        
             
        
