class Solution:
    def fib(self, n: int) -> int:
        
        # base cases
        if n == 0 or n == 1:
            return n
        
        # return sum of the two preceding Fibonacci numbers
        return self.fib(n-1) + self.fib(n-2)
