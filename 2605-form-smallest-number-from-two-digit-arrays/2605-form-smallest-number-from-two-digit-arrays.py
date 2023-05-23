class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        j1 = 0
        j2 = 0
        while j1<len(nums1) and j2<len(nums2):
            if nums1[j1] == nums2[j2]:
                return nums1[j1]
            elif nums1[j1] < nums2[j2]:
                j1 += 1
            else:
                j2 += 1
        return min(10*nums1[0]+nums2[0], 10*nums2[0]+nums1[0])
        