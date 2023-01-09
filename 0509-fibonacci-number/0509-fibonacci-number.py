class Solution:
    def __init__(self):
        self.memo = {}
    def fib(self, n: int) -> int:
        
        # base cases
        if n == 0 or n == 1:
            return n
        
        if n-1 not in self.memo: self.memo[n-1] = self.fib(n-1)
        if n-2 not in self.memo: self.memo[n-2] = self.fib(n-2)
        
        # return sum of the two preceding Fibonacci numbers
        return self.memo[n-1] + self.memo[n-2]
