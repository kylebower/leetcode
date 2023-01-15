class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        
        distance = 0
        
        for i, val in enumerate(arr1):
            if self.distBool(val,arr2,d):
                distance += 1
                
        return distance
    
    def distBool(self, val, arr2, d):
        for v in arr2:
            if abs(val-v) <= d:
                return False
        return True