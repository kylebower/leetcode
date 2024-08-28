class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.d = dict()
        self.n = len(grid)
        for i in range(self.n):
            for j in range(self.n):
                val = grid[i][j]
                self.d[val] = [i,j]
        

    def adjacentSum(self, value: int) -> int:
        [i,j] = self.d[value]        
        res = 0
        if i > 0:
            res += self.grid[i-1][j]
        if i < self.n - 1:
            res += self.grid[i+1][j]
        if j > 0:
            res += self.grid[i][j-1]
        if j < self.n - 1:
            res += self.grid[i][j+1]
        return res
                

    def diagonalSum(self, value: int) -> int:
        [i,j] = self.d[value]        
        res = 0
        if i > 0 and j > 0:
            res += self.grid[i-1][j-1]
        if i < self.n - 1 and j < self.n - 1:
            res += self.grid[i+1][j+1]
        if i < self.n - 1 and j > 0:
            res += self.grid[i+1][j-1]
        if i > 0 and j < self.n - 1:
            res += self.grid[i-1][j+1]
        return res
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)