class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = [c for c in s]
        count_I = 0
        count_D = 0
        n = len(s)
        for i, c in enumerate(res):            
            if c == 'I':
                res[i] = count_I
                count_I += 1
            elif c == 'D':
                res[i] = n - count_D
                count_D += 1
        res += [count_I]
        return res
    