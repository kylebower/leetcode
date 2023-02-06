class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for n in range(left, right+1):
            if self.selfdividing(n):
                res.append(n)
        
        return res
    
    def selfdividing(self, n):
        x = n
        while x > 0:
            digit = x%10
            if digit == 0:
                return False
            x //= 10
            if (n % digit) != 0:
                return False
        return True
        