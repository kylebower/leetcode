class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 1
        while power < n:
            power *= 3
        return power == n