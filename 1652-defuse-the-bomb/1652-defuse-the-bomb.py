class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        plain = [0]*n
        
        if k == 0:
            plain = [0]*n
        elif k > 0:
            cur = sum(code[:k])
            for i in range(n):
                cur -= code[i]
                cur += code[(i+k)%n]
                plain[i] = cur
        else:   # k < 0:
            cur = sum(code[n+k:])
            for i in range(n):
                plain[i] = cur
                cur += code[i]
                cur -= code[(i+k)%n]
        
        return plain
        