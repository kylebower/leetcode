class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for s in strs:
            if s.isdigit():
                value = int(s)
            else:
                value = len(s)
            res = max(res, value)
        return res
    