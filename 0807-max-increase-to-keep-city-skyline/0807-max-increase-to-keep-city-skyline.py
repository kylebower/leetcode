class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        # define size of city
        n = len(grid)
        
        # define arrays of skyline height for each row and col
        sh_r = [0]*n
        sh_c = [0]*n
        
        # compute skyline height for each row and col
        for r in range(n):
            for c in range(n):
                cur = grid[r][c]
                if cur > sh_r[r]:
                    sh_r[r] = cur
                if cur > sh_c[c]:
                    sh_c[c] = cur
        
        # compute max total allowed increase
        res = 0
        for r in range(n):
            for c in range(n):
                cur = grid[r][c]
                res += min(sh_r[r], sh_c[c]) - cur
        
        # return max total sum that the height of the buildings can be increased by without changing the city's skyline
        return res        
        