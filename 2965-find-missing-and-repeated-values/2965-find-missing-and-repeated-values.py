class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0]*2
        n = len(grid)
        
        counts = {}
        for row in grid:
            for elem in row:
                counts[elem] = counts.get(elem,0) + 1
                
        for k in range(1,n**2+1):
            if k not in counts:
                ans[1] = k
            elif counts[k] == 2:
                ans[0] = k
        
        return ans
                