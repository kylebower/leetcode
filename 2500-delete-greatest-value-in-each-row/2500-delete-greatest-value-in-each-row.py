class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # sort each row
        for i,row in enumerate(grid):
            new_row = sorted(row)
            grid[i] = new_row
        
        # add max of each col to result
        res = 0
        for i in range(len(grid[0])):
            res += max([gridk[i] for gridk in grid])
        
        # return result
        return res
    