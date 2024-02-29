class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        for k in range(1,n+1):
            d[self.sumDigits(k)] += 1
        
        largest_size = max(list(d.values()))
        res = 0
        for value in list(d.values()):
            if value == largest_size:
                res += 1
        return res
    
    def sumDigits(self, k: int) -> int:
        res = 0
        while k > 0:
            last_digit = k%10
            res += last_digit
            k //= 10
        return res
    