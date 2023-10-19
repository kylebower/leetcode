class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices
        for i, price in enumerate(prices):
            discount = 0
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            res[i] -= discount
        return res