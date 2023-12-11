class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        target = sum(arr) / 3        
        cur = 0
        count = 0
        
        for num in arr:
            cur += num
            if cur == target:
                count += 1
                cur = 0
            if count == 3:
                return True
        
        return False
        