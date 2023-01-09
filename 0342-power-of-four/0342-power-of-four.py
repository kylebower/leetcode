class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = 1
        while num < n:
            num *= 4
        return num == n