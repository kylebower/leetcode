class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        for i in range(n):
            row_i = sorted(matrix[i])
            col_i = sorted([row[i] for row in matrix])
            if row_i != list(range(1,n+1)):
                return False
            if col_i != list(range(1,n+1)):
                return False
        
        return True