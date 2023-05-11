class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # sort citations in decreasing order
        citations.sort()
        citations = citations[::-1]
        
        # compute max h-index
        h = 0
        for i, cit in enumerate(citations):
            if cit >= i+1:
                h = i+1
            else:
                break
        
        # return h-index
        return h