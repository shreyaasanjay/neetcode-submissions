class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n+1)

        sum = 0
        dp[0]=1
        dp[1]=1
        
        for i in range(1, n):
            print(i)
            if i<len(dp):
                dp[i+1]= dp[i]+dp[i-1]


        return dp[-1]


# wait so theres an array and the first two indexes are 1 and the next index is the last two indexes summed (lowk like fibonacci)