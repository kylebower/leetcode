class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # (mxn) integer matrix
        m = len(matrix)
        n = len(matrix[0])
        
        # find correct row (binary search)
        L = 0
        R = m-1
        while L + 1 < R:
            mid = int(L + (R-L)/2)
            if matrix[mid][0] <= target:
                L = mid
            else:
                R = mid-1
        if matrix[R][0] <= target:
            row = R
        else:
            row = L        
        
        # find correct col (binary search)
        L = 0
        R = n-1
        while L+1 < R:
            mid = int(L + (R-L)/2)
            if matrix[row][mid] <= target:
                L = mid
            else:
                R = mid-1
        
        # return true if target is in matrix or false otherwise
        return matrix[row][L] == target or matrix[row][R] == target
    