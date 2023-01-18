class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        d1 = {}
        d2 = {}
        
        for n1 in nums1:
            d1[n1] = 1
        for n2 in nums2:
            d2[n2] = 1
            
        for n in d1:
            if n in d2:
                result.append(n)
        
        return result
