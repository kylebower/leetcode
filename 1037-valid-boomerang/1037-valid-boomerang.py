class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # define points
        p0 = points[0]
        p1 = points[1]
        p2 = points[2]
        
        # define direction vectors
        d1 = [p0[0]-p1[0],p0[1]-p1[1]]
        d2 = [p0[0]-p2[0],p0[1]-p2[1]]
        
        # define normal vector
        n2 = [d2[1], -d2[0]]
        
        # if d1 \cdot n2 != 0, boomerang
        return d1[0]*n2[0]+d1[1]*n2[1] != 0        
