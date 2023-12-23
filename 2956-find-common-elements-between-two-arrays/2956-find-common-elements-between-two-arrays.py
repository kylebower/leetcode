class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # define variables
        n = len(nums1)
        m = len(nums2)
        count1 = 0
        count2 = 0
        set1 = set(nums1)
        set2 = set(nums2)
        
        # count The number of indices i such that 0 <= i < n and nums1[i] occurs at least once in nums2.
        for i in range(n):
            if nums1[i] in set2:
                count1 += 1
        
        # count The number of indices i such that 0 <= i < m and nums2[i] occurs at least once in nums1.
        for i in range(m):
            if nums2[i] in set1:
                count2 += 1
        
        # Return an integer array answer of size 2 containing the two values in the above order.
        return [count1, count2]
    