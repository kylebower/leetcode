class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # define output array
        res = []
        
        # add all cells to output array
        for r in range(rows):
            for c in range(cols):
                res.append([r,c])
        
        # sort cells by distance from (rCenter, cCenter)
        res.sort(key = lambda x: abs(x[0]-rCenter) + abs(x[1]-cCenter))
        
        # Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter)
        return res
    
    # time complexity: O(rows*cols*log(rows*cols))
    # space complexity: O(1)
    