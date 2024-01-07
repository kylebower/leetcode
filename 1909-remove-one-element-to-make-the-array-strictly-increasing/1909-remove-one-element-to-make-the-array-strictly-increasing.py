class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            cur = nums[:i] + nums[i+1:]
            if self.isSorted(cur):
                return True
        return False
    
    def isSorted(self, arr: List[int]) -> bool:
        # return True if arr is strictly increasing
        # otherwise return False
        m = len(arr)
        for j in range(m-1):
            if arr[j] >= arr[j+1]:
                return False
        return True
    