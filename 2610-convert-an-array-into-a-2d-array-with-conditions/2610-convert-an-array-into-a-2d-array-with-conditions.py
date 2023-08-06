class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # make dict of occurences of each number in nums
        d = dict()
        for n in nums:
            d[n] = d.get(n,0) + 1
        
        # iterate to create rows in output array
        res = []
        while d:
            row = []
            for k in list(d.keys()):
                row.append(k)
                d[k] = d.get(k,0) - 1
                if d[k] == 0:
                    # remove k from d
                    d.pop(k)
            res.append(row)
        
        # return output array
        return res
    