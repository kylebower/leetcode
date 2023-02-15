class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # define dictionary of frequencies
        d = {}
        
        # populate dictionary
        for n in nums:
            d[n] = d.get(n,0)+1
        
        # sort array by increasing frequency
        freq = [0]*len(nums)
        for i in range(len(nums)):
            freq[i] = d[nums[i]]
        
        m_nums = [-x for x in nums]
        m_res = [y for x,y in sorted(zip(freq,m_nums))]
        res = [-x for x in m_res]
        
        # return sorted array
        return res
    