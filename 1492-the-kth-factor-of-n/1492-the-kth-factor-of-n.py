class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        num_factors = 0
        for i in range(1,n+1):
            if n%i == 0:
                num_factors += 1
            if num_factors == k:
                return i
        return -1
    
    # time complexity: O(n)
    # space complexity: O(1)
    