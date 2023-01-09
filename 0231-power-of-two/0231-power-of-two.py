class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 1
        while power < n:
            power *= 2
        return power == n