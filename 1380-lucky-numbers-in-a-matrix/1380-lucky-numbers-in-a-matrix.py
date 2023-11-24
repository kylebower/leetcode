import numpy as np

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # define output array
        res = []
        
        # define number of rows and cols
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            # for each row find minimum value and index
            value_min = min(matrix[i])
            index_min = np.argmin(matrix[i])
            
            # check if it is the max of the col
            col_max = max([x[index_min] for x in matrix])
                        
            # if max of col append to output array
            if value_min == col_max:
                res.append(value_min)
        
        # return output array
        return res
