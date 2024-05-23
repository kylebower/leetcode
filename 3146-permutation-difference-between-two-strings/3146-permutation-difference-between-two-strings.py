class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ds = dict()
        for i,c in enumerate(s):
            ds[c] = i
            
        dt = dict()
        for i,c in enumerate(t):
            dt[c] = i        
        
        permutationDifference = 0
        for key in dt:
            permutationDifference += abs(dt[key] - ds[key])
        
        return permutationDifference
    