class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0]*2
        n = len(grid)
        
        entries = set()
        for row in grid:
            for entry in row:
                if entry in entries:
                    ans[0] = entry
                else:
                    entries.add(entry)
                
        for k in range(1,n**2+1):
            if k not in entries:
                ans[1] = k
                break
        
        return ans
                