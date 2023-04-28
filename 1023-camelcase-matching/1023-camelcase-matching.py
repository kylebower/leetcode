class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        res = []
        for q in queries:
            print(q)
            res.append(self.match(q, pattern))
        return res
    
    def isUpper(self, c):
        return ord(c) >= ord('A') and ord(c) <= ord('Z')
    
    def match(self, q: str, pattern: str):        
        # define two pointers
        p1, p2 = 0, 0
        while p1 < len(q) and p2 < len(pattern):
            while p1 < len(q) and q[p1] != pattern[p2]:
                if self.isUpper(q[p1]):
                    return False
                else:
                    p1 += 1
            if p1 < len(q) and p2 < len(pattern):
                p2 += 1
                p1 += 1
        if p2 < len(pattern):
            return False
        while p1 < len(q):
            if self.isUpper(q[p1]):
                    return False
            p1 += 1
        return True
                