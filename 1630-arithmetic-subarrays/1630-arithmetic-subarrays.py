class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [0]*len(l)
        for k in range(len(l)):
            cur = nums[l[k]:r[k]+1]
            cur.sort()
            res[k] = self.isArithmetic(cur)
        return res
    
    def isArithmetic(self, cur: List[int]) -> bool:
        step = cur[1]-cur[0]
        for k in range(len(cur)-1):
            if cur[k+1] - cur[k] != step:
                return False
        return True
        