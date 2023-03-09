class Solution:
    def digitCount(self, num: str) -> bool:
        
        # define length of num
        n = len(num)
        
        # make dict of occurances of each digit in num
        d = {}
        for c in num:
            d[int(c)] = d.get(int(c), 0) + 1
        
        # check that digit i occurs num[i] times in num
        for i in range(n):
            if i not in d:
                if num[i] == '0':
                    continue
                else:
                    return False
            elif d[i] != int(num[i]):
                return False
        
        return True
    