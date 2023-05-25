class Solution:
    def largestInteger(self, num: int) -> int:
        arr = [int(x) for x in str(num)]
        
        even, odd = [], []
        for x in arr:
            if x%2==1:
                odd.append(x)
            else:
                even.append(x)
        odd.sort()
        even.sort()
        
        res = 0
        for x in arr:
            if x%2==1:
                res = 10*res + odd.pop()
            else:
                res = 10*res + even.pop()
        
        return res
    