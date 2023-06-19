class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # mat in an mxn matrix
        m = len(mat)
        n = len(mat[0])
        
        # define indices of matrix
        indices = [i for i in range(m)]
        
        # define strengths of each row in matrix
        strengths = [sum(row) for row in mat]
        
        # zip strengths and indices together
        str_ind = zip(strengths, indices)
        
        # find indices of rows in the matrix ordered from weakest to strongest
        sorted_ind = [y for _,y in sorted(str_ind)]
        
        # Return the indices of the k weakest rows in the matrix ordered from weakest to strongest
        return sorted_ind[:k]
    