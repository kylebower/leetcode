class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        nRow = len(grid)
        nCol = len(grid[0])
        nNeg = 0
        
        # start in top right corner
        nR = 0
        nC = nCol-1
        
        # iterate to find number of negative numbers in each row
        while nC >= 0 and nR < nRow:
            while nC > 0 and grid[nR][nC] < 0:
                nC -= 1
            nNeg += nCol-1-nC + 1*(grid[nR][nC] < 0)
            nR += 1
        
        # return the number of negative numbers in grid.
        return nNeg
        
        
        