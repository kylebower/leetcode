import numpy as np
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = np.arange(lo, hi+1)
        arr = sorted(arr, key = lambda x: self.power(x))
        return arr[k-1]
    
    def power(self, x: int) -> int:
        # return power value of x
        res = 0
        while x > 1:
            if x%2==0:
                x = x / 2
            else:
                x = 3*x + 1
            res += 1
        return res