class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        nPoints = len(points)
        nQueries = len(queries)
        answer = [0]*nQueries
        
        for j, qj in enumerate(queries):
            for pi in points:
                if self.pointInCircle(pi,qj):
                    answer[j] += 1
        
        return answer
    
    def pointInCircle(self, p, q):
        return (p[0]-q[0])**2 + (p[1]-q[1])**2 <= q[2]**2
