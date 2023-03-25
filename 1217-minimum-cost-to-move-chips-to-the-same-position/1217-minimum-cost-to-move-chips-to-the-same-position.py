class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count_0mod2 = 0
        count_1mod2 = 0
        
        for p in position:
            if p%2==0:
                count_0mod2 += 1
            else:
                count_1mod2 += 1
        
        return min(count_0mod2,count_1mod2)
    