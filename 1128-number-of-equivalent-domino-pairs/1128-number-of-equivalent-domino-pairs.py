class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        # base case
        if n < 2:
            return 0
        
        # define dict of dominoes found sorted with smaller number first
        d = {}
        for domino in dominoes:
            domino.sort()
            cur = (domino[0],domino[1])
            d[cur] = d.get(cur,0)+1
            
        # count number of pairs of equivalent dominoes
        res = 0
        for key in d:
            res += d[key]*(d[key]-1)//2   # nC2 = n!/((n-2)!*2!) = n(n-1)/2
            
        # return number of pairs of equivalent dominoes
        return res
    