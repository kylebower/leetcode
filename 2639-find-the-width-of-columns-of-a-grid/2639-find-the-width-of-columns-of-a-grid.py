class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # define number of rows and cols of grid
        m = len(grid)
        n = len(grid[0])
        
        # define output array
        ans = [0]*n
        
        # iterate to compute width of the ith column
        for i in range(n):
            ans[i] = max([len(str(grid[k][i])) for k in range(m)])
        
        # return output array
        return ans
    