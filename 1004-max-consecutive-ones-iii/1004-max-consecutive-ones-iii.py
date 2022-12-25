class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # base case
        n = len(nums)
        if n <= k:
            return n
        
        # define pointers
        L = 0
        R = 0
        
        # count number of 0's
        counter = 0
        
        max_length = 0
        
        # iterate to find max_length
        while R < n:
            if nums[R] == 0:
                counter += 1
            while counter > k:
                if nums[L] == 0:
                    counter -= 1
                L += 1
            max_length = max(max_length, R - L + 1)
            R += 1
        
        # return maximum number of consecutive 1's in the array if you can flip at most k 0's
        return max_length
