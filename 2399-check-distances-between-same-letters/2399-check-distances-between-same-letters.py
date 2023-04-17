class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        d = {}
        n = len(s)
        for i in range(n):
            c = s[i]
            if c not in d:
                d[c] = i
            else:
                if i-d[c]-1 != distance[ord(c)-ord('a')]:
                    return False                
        return True
            