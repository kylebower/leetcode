class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        res = 0
        piles.sort()
        piles = piles[::-1]
        for i in range(1,int(2*len(piles)/3),2):
            res += piles[i]
        return res
    