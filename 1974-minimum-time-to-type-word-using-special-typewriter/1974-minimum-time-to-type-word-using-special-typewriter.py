class Solution:
    def minTimeToType(self, word: str) -> int:
        cur = 'a'
        res = 0
        for c in word:
            stepSize = min(abs(ord(c) - ord(cur)), 26 - abs(ord(c) - ord(cur)))
            res += stepSize + 1
            cur = c
        return res
    