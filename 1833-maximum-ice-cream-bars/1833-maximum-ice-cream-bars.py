class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse = 1)
        
        bars = 0
        while coins and costs:
            if coins>=costs[-1]:
                coins -= costs.pop()
                bars += 1
            else:
                return bars
        
        return bars
    