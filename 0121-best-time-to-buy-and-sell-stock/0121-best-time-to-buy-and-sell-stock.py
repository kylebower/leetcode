class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # base case
        n = len(prices)
        if n == 1:
            return 0
        
        # find max price on or after each day
        max_price_on_or_after = [nan]*n
        max_price_on_or_after[n-1] = prices[n-1]
        for i in range(n-2,-1,-1):
            max_price_on_or_after[i] = max(prices[i], max_price_on_or_after[i+1])
        
        # find max profit
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_price_on_or_after[i]-prices[i])
        
        # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
        return max_profit
