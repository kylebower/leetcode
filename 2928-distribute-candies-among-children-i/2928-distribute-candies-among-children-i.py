class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        number_ways = 0
        for i in range(n+1):
            for j in range(n+1-i):
                k = n - i - j
                if max(i,j,k) <= limit:
                    number_ways += 1
        return number_ways
    