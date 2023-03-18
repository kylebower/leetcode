class Solution:
    def countAsterisks(self, s: str) -> int:
        between_bars = False
        res = 0
        for c in s:
            if c == '|':
                between_bars = not between_bars
            elif c == '*' and not between_bars:
                res += 1
        return res
    
    # time complexity: O(n)
    # space complexity: O(1)
    