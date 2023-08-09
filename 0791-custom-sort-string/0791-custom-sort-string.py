class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        return ''.join(sorted(s, key = lambda x: d.get(x,math.inf)))