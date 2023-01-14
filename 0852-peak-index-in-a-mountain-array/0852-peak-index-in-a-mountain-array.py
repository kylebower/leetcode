class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # define two pointers
        L = 0
        R = n-1
        
        while L+2 < R:
            mid = int((R+L)/2)
            midp1 = mid + 1
            if arr[midp1] > arr[mid]:
                L = mid
            else:
                R = midp1
                
        mid = int((R+L)/2)
        if arr[L] >= max(arr[R], arr[mid]):
            return L
        elif arr[R] >= max(arr[L], arr[mid]):
            return R
        else:
            return mid
    # time complexity: O(logn)
    # space complexity: O(1)
