class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while n!=1:
            dummy = n
            n = 0
            for i in str(dummy):
                n = n + int(i)**2
            print(n)
            count = count +1
            if count>1000:
                return False

        return True