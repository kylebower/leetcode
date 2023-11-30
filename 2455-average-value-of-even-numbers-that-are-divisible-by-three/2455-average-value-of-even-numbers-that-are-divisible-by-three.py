import math
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum_even3 = 0
        num = 0
        for n in nums:
            if n%6 == 0:
                num += 1
                sum_even3 += n
        if num == 0:
            return 0
        else:
            return math.floor(sum_even3/num)