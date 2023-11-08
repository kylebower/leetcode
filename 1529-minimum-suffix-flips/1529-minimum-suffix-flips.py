class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        pre = 0
        for c in target:
            if int(c) == pre:
                continue
            else:
                pre = int(c)
                res += 1
        return res
            