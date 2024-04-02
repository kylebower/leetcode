class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = -1
        n = len(nums)
        
        for i in range(n):
            for j in range(i,n):
                if self.isStrongPair(nums[i], nums[j]):
                    res = max(res, self.xor(nums[i], nums[j]))
        
        return res
    
    def isStrongPair(self, x:int , y:int ) -> bool:
        # return True if x and y form a strong pair
        # otherwise return False
        return abs(x-y) <= min(x,y)
    
    def xor(self, x: int, y:int) -> int:
        # return bitwise XOR or x and y
        return x ^ y
    