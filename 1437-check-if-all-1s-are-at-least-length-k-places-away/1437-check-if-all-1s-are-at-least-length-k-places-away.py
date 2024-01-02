class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -inf
        for i, val in enumerate(nums):
            if val == 1:
                if i - prev - 1 < k:
                    return False
                else:
                    prev = i
        return True
                