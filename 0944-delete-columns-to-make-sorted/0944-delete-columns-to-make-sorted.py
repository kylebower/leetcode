class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        count = 0
        
        for i in range(m):
            cur = [x[i] for x in strs]
            temp = sorted(cur)
            if cur != temp:
                count += 1
        
        return count
    