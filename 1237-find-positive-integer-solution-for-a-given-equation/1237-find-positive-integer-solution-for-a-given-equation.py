"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        for x in range(1,1001):
            ymin = 1
            ymax = 1000
            while ymin + 1 < ymax:
                mid = int(ymin+(ymax-ymin)/2)
                cur = customfunction.f(x, mid)
                if cur == z:
                    break
                elif cur < z:
                    ymin = mid
                else:
                    ymax = mid
            mid = int(ymin+(ymax-ymin)/2)
            if customfunction.f(x, mid) == z:
                res.append([x,mid])
            elif customfunction.f(x, mid+1) == z:
                res.append([x,mid+1])
        return res
    