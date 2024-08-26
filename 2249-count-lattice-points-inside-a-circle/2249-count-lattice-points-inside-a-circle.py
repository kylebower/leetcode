class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        max_x = max([c[0] for c in circles]) + max([c[2] for c in circles])
        max_y = max([c[1] for c in circles]) + max([c[2] for c in circles])
        res = 0
        
        for i in range(max_x + 1):
            for j in range(max_y + 1):
                for c in circles:
                    if self.inCircle(c, i, j):
                        res += 1
                        break
        
        return res
    
    def inCircle(self, c, i ,j):
        return (c[0] - i)**2 + (c[1] - j)**2 <= c[2]**2
    