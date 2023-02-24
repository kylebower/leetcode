class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # define number of pairs
        n = len(nums) // 2
        
        # define previous list
        pre = []
        
        # iterate through each pair
        for i in range(n):
            # make current list
            freq, val = nums[2*i], nums[2*i+1]
            cur = [val] * freq
            
            # append current list to previous
            pre += cur
            
        # return decompressed list
        return pre
        