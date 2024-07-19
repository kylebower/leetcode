class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        cnt = collections.Counter(nums)
        
        while cnt:
            m = min(cnt)
            for i in range(m, m+k):
                if i not in cnt:
                    return False
                elif cnt[i] == 1:
                    del cnt[i]
                else:
                    cnt[i] -= 1
                    
        return True
    