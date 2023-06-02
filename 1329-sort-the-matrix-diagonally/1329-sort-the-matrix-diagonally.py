class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        # define dim of matrix
        m = len(mat)    # num rows
        n = len(mat[0]) # num cols
        
        # make dict of entries on each diagonal
        d = defaultdict(list)
        for mi in range(m):
            for ni in range(n):
                key = ni-mi
                d[key].append(mat[mi][ni])
        
        # sort diagonals
        for key in d:
            d[key].sort(reverse=1)
            
        # construct output matrix        
        for mi in range(m):
            for ni in range(n):
                key = ni-mi
                mat[mi][ni] = d[key].pop()
        
        # return sorted matrix
        return mat
        