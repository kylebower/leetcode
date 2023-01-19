class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set()
        num_triplets = 0
        for n in nums:
            if n-diff in nums_set and n-2*diff in nums_set:
                num_triplets += 1
            nums_set.add(n)
        return num_triplets
    
    # time complexity: O(n)
    # space complexity: O(n)
                