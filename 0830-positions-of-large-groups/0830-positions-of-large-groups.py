class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # define output array
        res = []
        
        # define two pointers
        n = len(s)
        L = 0
        R = 0
        
        # move sliding window to find positions of large groups
        while L<n:
            while R<n and s[L] == s[R]:
                R += 1
            if R-L >= 3:
                res.append([L,R-1])
            L = R
        
        # Return the intervals of every large group sorted in increasing order by start index
        return res
    