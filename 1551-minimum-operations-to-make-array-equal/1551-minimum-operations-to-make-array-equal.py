class Solution:
    def minOperations(self, n: int) -> int:
        
        N = n//2
        return N*(N+1) if n%2==1 else N*N
    