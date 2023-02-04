class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            time += self.time_pq(points[i], points[i+1])
        
        return time
    
    def time_pq(self, p, q):
        return max(abs(p[0]-q[0]), abs(p[1]-q[1]))
    