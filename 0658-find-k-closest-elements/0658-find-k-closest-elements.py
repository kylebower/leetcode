class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n = len(arr)
        
        # base case
        if n == 1:
            return arr
        
        # define pointers
        L, R = 0, n-1
        
        # perform binary search to find index of closest int in arr to x
        index = None
        while L+1 < R:
            mid = int((L+R)/2)
            if arr[mid] == x:
                index = mid
                break
            elif arr[mid] < x:
                L = mid
            else:
                R = mid
        
        # select index of closest int in arr to x
        if index is None:
            if abs(arr[L]-x) <= abs(arr[R]-x):
                index = L
            else:
                index = R
            
        # expand outwards to find k closest int to x in arr
        left = index
        right = index
        counter = 1
        while counter < k:
            if left == 0:
                right += 1
            elif right == n-1:
                left -= 1
            elif abs(arr[left-1]-x) <= abs(arr[right+1]-x):
                left -= 1
            else:
                right += 1
            counter += 1
        
        # return the k closest integers to x in the array
        # result should also be sorted in ascending order.
        result = arr[left:right+1]
        return result
            