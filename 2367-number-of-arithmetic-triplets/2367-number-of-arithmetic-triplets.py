class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        num_triplets = 0
        for n in nums_set:
            if n+diff in nums_set and n+2*diff in nums_set:
                num_triplets += 1
        return num_triplets
                