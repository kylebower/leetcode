class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # greedy alg: 
        # let M = max(nums)
        # choose M, M+1, ..., M + (k-1)
        M = max(nums)
        # return k*M + sum(0,1,...,k-1)
        return int(k*M + k*(k-1)/2)
    
    # time complexity: O(n)
    # space complexity: O(1)
    