import numpy as np
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        result = -1
        smallest_so_far = float('inf')
        n = len(points)
        for i in range(n):
            p = points[i]
            if checkPValid(x,y,p):
                manhat = np.linalg.norm([p[0]-x,p[1]-y])
                if manhat < smallest_so_far:
                    smallest_so_far = manhat
                    result = i
        return result

def checkPValid(x,y,p):
    return p[0] == x or p[1] == y