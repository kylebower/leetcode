class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
                
        aliceTotal = sum(aliceSizes)
        bobTotal = sum(bobSizes)
        
        diff = (aliceTotal - bobTotal)/2
        
        for b in bobSizes:
            if b+diff in set(aliceSizes):
                return [b+diff,b]
            