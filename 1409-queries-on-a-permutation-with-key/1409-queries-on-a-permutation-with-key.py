class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # define permutation P
        P = [x for x in range(1,m+1)]
        
        # define result array
        res = []
        
        # iterate through queries, permute P
        for q in queries:
            index = P.index(q)
            res.append(index)
            P = [q] + P[:index] + P[index+1:]
        
        # return result
        return res
    