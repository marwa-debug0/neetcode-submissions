class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) 
        profits = set()

        if n == 1: 
            return 0 

        for i in range(n - 1):
            for j in range(i, n):
                buy = prices[i] ; sell = prices[j]
                if sell - buy > 0: 
                    profits.add(sell - buy)
                else : 
                    profits.add(0)
        
        return max(profits)
        
