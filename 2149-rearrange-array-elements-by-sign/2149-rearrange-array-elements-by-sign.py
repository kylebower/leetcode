class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # define two pointers
        pos = 0
        neg = 0
        
        # define length of nums, output array, and counter
        n = len(nums)        
        res = [0]*n
        i = 0
        
        # iterate to rearrange list
        while i < n:
            # find next pair
            while nums[pos] < 0:
                pos += 1
            while nums[neg] > 0:
                neg += 1
            
            # add pair to result
            res[i] = nums[pos]
            res[i+1] = nums[neg]
            
            # increment counters
            pos += 1
            neg += 1
            i += 2
        
        # return modified array
        return res
    
    # time complexity: O(n)
    # space complexity: O(n)