class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        [x11, y11, x12, y12] = rec1
        [x21, y21, x22, y22] = rec2
        
        return self.intersect(x11, x12, x21, x22) and self.intersect(y11, y12, y21, y22)
    
    def intersect(self, x11, x12, x21, x22):
        return max(x11, x21) < min(x12, x22)