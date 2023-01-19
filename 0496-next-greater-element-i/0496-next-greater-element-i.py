class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # define lengths of input arrays
        n1 = len(nums1)
        n2 = len(nums2)
        
        # define output array
        ans = [0]*n1
        
        # For each 0 <= i < n1
        for i in range(n1):
            # find the index j such that nums1[i] == nums2[j]
            j = self.findIndexJ(nums1[i], nums2)
        
            # determine the next greater element of nums2[j] in nums2.
            # If there is no next greater element, -1                
            ans[i] = self.findNextGreater(j,nums2)
        
        # Return an array ans of length n1 such that ans[i] is the next greater element
        return ans
    
    def findNextGreater(self, j, nums2):
        nums2j = nums2[j]
        while j < len(nums2):
            if nums2[j]> nums2j:
                return nums2[j]
            j += 1
        return -1
    
    def findIndexJ(self, target, nums2):
        j = 0
        while nums2[j] != target:            
            j += 1
        return j
