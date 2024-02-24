class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        b = n-1
        while '0' in str(a) + str(b):
            a += 1
            b -= 1
        return [a, b]
    