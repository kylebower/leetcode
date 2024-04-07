class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        j = m-1
        k = n-1
        res = 1
        for i in range(1,j+1):
            res *= k+i
        return int(res / math.factorial(j))
    