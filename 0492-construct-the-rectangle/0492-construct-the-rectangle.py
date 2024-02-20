class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = 1
        L = area
        
        for k in range(1,int(sqrt(area))+1):
            if area%k == 0:
                W = k
                L = area // k
        
        return [L, W]
    