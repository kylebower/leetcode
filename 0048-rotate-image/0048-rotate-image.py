class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # flip matrix up down
        n = len(matrix)
        for i in range(n//2):
            temp = matrix[i]
            matrix[i] = matrix[n-1-i]
            matrix[n-1-i] = temp
        
        # take transpose
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        