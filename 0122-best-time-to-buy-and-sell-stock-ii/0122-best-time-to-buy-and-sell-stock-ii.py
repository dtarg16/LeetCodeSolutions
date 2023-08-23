class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, buy, sell, profit, n = 0, 0, 0, 0, len(prices) - 1
        
        while i < n:
            while i < n and prices[i] >= prices[i+1]:
                i += 1
            buy = prices[i]
            
            while i < n and prices[i] < prices[i+1]:
                i += 1
            sell = prices[i]
            
            profit += sell - buy
            
        return profit
