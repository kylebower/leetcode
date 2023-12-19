class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # define variables
        m = len(matrix)     # rows
        n = len(matrix[0])  # cols
        
        # iterate to check if matrix is Toeplitz
        i0 = 0
        j0 = 0
        for diag in range(1-m,n):
            if diag < 0:
                i0 = -diag
                j0 = 0
            else:
                i0 = 0
                j0 = diag
                
            value = matrix[i0][j0]
            while i0 < m and j0 < n:
                # return false if the matrix is NOT Toeplitz
                if matrix[i0][j0] != value:
                    return False
                i0 += 1
                j0 += 1
        
        # return true if the matrix is Toeplitz
        return True
    