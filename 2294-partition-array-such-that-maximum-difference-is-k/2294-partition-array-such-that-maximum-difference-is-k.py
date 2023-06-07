class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        cur_start = nums[0]
        for i,n in enumerate(nums):
            if n - cur_start > k:
                if i < len(nums):
                    cur_start = nums[i]
                res += 1
        return res
        