class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profits = [0] * len(prices)
        profit = 0;
        for i in range (len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i]>profit:
                    profit = prices[j]-prices[i]
                max_profits[i] = profit
        max_profit = 0
        for i in range(len(max_profits)):
            if max_profits[i]>max_profit:
                max_profit=max_profits[i]
        
        if max_profit<0:
            return 0
        return max_profit
        