class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res = 0
        max_end_so_far = 0
        nums.sort()
        
        for num in nums:            
            # update result
            if num[1] > max_end_so_far:
                res += min(num[1] - num[0] + 1, num[1] - max_end_so_far)
            
            # update max end so far
            max_end_so_far = max(max_end_so_far ,num[1])
            
        return res