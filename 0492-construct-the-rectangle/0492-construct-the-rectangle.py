class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = 1
        L = area
        
        w = W
        l = L
        
        while w <= l:
            cur = w*l
            if cur == area:
                W = w
                L = l
                w += 1
            elif cur > area:
                l -= 1
            else:
                w += 1
        
        return [L, W]
    