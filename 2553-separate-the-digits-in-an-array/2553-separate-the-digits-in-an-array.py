class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        str_nums = [str(n) for n in nums]
        str_num = ''.join(str_nums)
        return [int(c) for c in str_num]