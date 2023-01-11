import numpy as np
import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        # define largest_area
        largest_area = 0
        
        # define number of points
        n = len(points)
        
        # brute force approach
        for i1 in range(n-2):
            for i2 in range(i1+1,n-1):
                for i3 in range(i2+1,n):
                    # for each possible triangle, find area
                    area = computeArea(points[i1], points[i2], points[i3])
                    # update largest_area
                    if not math.isnan(area):
                        largest_area = max(area, largest_area)
        
        # return area of the largest triangle that can be formed by any three different points
        return largest_area

# compute area of triangle with vertices p1, p2, p3
def computeArea(p1, p2, p3):
    a = [p1[0]-p2[0], p1[1]-p2[1]]
    b = [p1[0]-p3[0], p1[1]-p3[1]]
    theta = np.arccos(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))
    area = 1/2 * np.linalg.norm(a) * np.linalg.norm(b) * np.sin(theta)
    return area
        