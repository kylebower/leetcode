class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        res = []
        for q in queries:
            res.append(self.match(q, pattern))
        
        return res
    
    def match(self, s: str, pattern: str):
        n = len(s)
        cur = 0
        for c in pattern:
            while cur < n and s[cur] != c:
                if ord(s[cur]) >= ord('A') and ord(s[cur]) <= ord('Z'):
                    return False
                cur += 1
            if cur == n:
                return False
            cur += 1
        
        for k in range(cur,n):
            c = s[k]
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                return False
        return True
                