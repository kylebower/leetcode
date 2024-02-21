class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        max_good = -1
        for i, c in enumerate(num[:-2]):
            if c == num[i+1] and c == num[i+2]:
                max_good = max(max_good, int(c))
        
        if max_good == -1:
            return ''
        else:
            return ''.join([str(max_good)]*3)
        