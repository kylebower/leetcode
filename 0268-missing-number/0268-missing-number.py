class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_first_n_nums = n*(n+1)/2
        
        return int(sum_of_first_n_nums - sum(nums))
