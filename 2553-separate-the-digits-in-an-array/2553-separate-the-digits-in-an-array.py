class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            cur = []
            for c in str(n):
                cur.append(int(c))
            res += cur
        return res