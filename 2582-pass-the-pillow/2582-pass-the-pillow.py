class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        index1 = time % (2*n-2)
        if index1 < n:
            index = index1+1
        else:
            index = 2*n-1 - index1
        return index
    