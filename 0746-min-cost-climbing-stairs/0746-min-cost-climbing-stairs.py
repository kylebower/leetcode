class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCostToEnd = [inf]*n
        minCostToEnd[n-1] = cost[n-1]
        minCostToEnd[n-2] = cost[n-2]
        for i in range(n-3,-1,-1):
            minCostToEnd[i] = cost[i]+min(minCostToEnd[i+1],minCostToEnd[i+2])
        
        return min(minCostToEnd[:2])
