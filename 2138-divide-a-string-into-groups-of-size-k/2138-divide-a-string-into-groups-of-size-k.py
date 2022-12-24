class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        result = []
        i = 0
        while i < n:
            if i+k <= n:
                result.append(s[i:i+k])
            else:
                result.append(s[i:] + fill*(k-(n-i)))
            i += k
        return result
