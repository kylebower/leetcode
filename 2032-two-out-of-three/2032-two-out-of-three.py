class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        n3 = len(nums3)
        
        d = {}
        for n in set(nums1):
            d[n] = d.get(n,0) + 1
        for n in set(nums2):
            d[n] = d.get(n,0) + 1
        for n in set(nums3):
            d[n] = d.get(n,0) + 1
        
        for k in list(d.keys()):
            if d[k] >= 2:
                result.append(k)
                
        return result                
            