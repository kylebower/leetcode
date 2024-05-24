class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0
        
        for c in s:
            if c == '(':
                depth += 1
                maxDepth = max(depth, maxDepth)
            elif c == ')':
                depth -= 1
        
        return maxDepth
    