class Solution:
    def partitionString(self, s: str) -> int:
        d = set()
        count = 1
        for c in s:
            if c in d:
                count += 1
                d = set(c)
            else:
                d.add(c)
        return count