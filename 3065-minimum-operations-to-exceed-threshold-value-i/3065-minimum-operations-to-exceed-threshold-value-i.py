class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        
        for num in nums:
            if num < k:
                result += 1
                
        return result
    