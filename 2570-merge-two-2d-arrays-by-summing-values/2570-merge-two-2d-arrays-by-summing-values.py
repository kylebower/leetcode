class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # define dict d[id] = val
        d = {}
        
        # update dict for each array
        for i in range(len(nums1)):
            d[nums1[i][0]] = nums1[i][1]
        for i in range(len(nums2)):
            d[nums2[i][0]] = d.get(nums2[i][0],0) + nums2[i][1]
        
        # define output array
        res = []
        ks = list(d.keys())
        ks.sort()
        for k in ks:
            res.append([k, d[k]])
        
        # Return the resulting array
        return res
    