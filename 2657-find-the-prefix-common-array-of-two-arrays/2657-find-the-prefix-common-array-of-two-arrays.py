class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0]*n
        
        set_a = set()
        set_b = set()
        
        for i in range(n):
            set_a.add(A[i])
            set_b.add(B[i])
            C[i] = len(set_a.intersection(set_b))
        
        return C
    