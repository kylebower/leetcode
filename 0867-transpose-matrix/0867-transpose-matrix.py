class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # matrix is nxm
        n = len(matrix)
        m = len(matrix[0])
        
        # result is mxn
        result = [[0 for _ in range(n)] for _ in range(m)]
        
        # compute transpose
        for ni in range(n):
            for mi in range(m):
                result[mi][ni] = matrix[ni][mi]
        
        return result
        
        