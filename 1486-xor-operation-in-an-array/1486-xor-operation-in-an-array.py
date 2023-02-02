class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0]*n
        for i in range(n):
            nums[i] = start + 2 * i
        
        result = 0
        for i in range(n):
            result ^= nums[i]
            
        return result
