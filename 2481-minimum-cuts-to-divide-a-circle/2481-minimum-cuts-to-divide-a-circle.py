class Solution:
    def numberOfCuts(self, n: int) -> int:
        # base case:
        if n == 1:
            return 0
        
        return n if n%2 else n//2
        
    # time complexity: O(1)
    # space complexity: O(1)
