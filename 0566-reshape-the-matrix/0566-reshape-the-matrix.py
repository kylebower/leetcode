import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # mat is an mxn matrix
        m = len(mat)
        n = len(mat[0])
        
        # base case: impossible params
        if r*c != m*n:
            return mat
        
        # define reshaped matrix
        reshaped_mat = [[0]*c]*r
        
        # populate reshaped matrix
        for i in range(r):
            reshaped_mat[i] = np.array(mat).flatten()[0+i*c:c+i*c]
        
        # return new reshaped matrix
        return reshaped_mat
        