class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        
        i1 = 0
        i2 = 0
        
        while i1 < n1 and i2 < n2:
            m1 = nums1[i1]
            m2 = nums2[i2]
            if m1 == m2:
                return m1
            elif m1 < m2:
                i1 += 1
            else:
                i2 += 1
        
        return -1
    
    # time complexity: O(n1 + n2)
    # space complexity: O(1)
    