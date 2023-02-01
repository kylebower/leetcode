class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # sort array
        arr.sort()
        
        zero_count = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                zero_count += 1
            else:
                if self.binarySearch(2*arr[i], arr):
                    return True
        
        return zero_count > 1
    
    def binarySearch(self, t, arr):
        L = 0
        R = len(arr) - 1
        
        while L+1 < R:
            mid = int(L + (R-L)/2)
            if arr[mid] == t:
                return True
            elif arr[mid] > t:
                R = mid
            else:
                L = mid
        
        return arr[L] == t or arr[R] == t
    
    # time complexity: O(nlogn)
    # space complexity: O(1)
