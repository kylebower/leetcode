class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        # find sum of primary and secondary matrix diagonals
        pri = 0
        sec = 0
        for i in range(n):
            pri += mat[i][i]
            pri += mat[i][n-i-1]
        
        # if n is odd, find middle element
        mid = 0
        if n%2 == 1:
            mid = mat[int((n-1)/2)][int((n-1)/2)]
        
        # return the sum of the matrix diagonals
        return pri + sec - mid

    # time complexity: O(n)
    # space complexity: O(1)
        