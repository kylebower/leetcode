class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # sort scores in decreasing order
        temp = sorted(score)[::-1]
        
        # create dict for ranks
        d = {}
        for i, tem in enumerate(temp):
            if i == 0:
                d[tem] = "Gold Medal"
            elif i == 1:
                d[tem] = "Silver Medal"
            elif i == 2:
                d[tem] = "Bronze Medal"
            else:
                d[tem] = str(i+1)
        
        # Return an array answer of size n where answer[i] is the rank of the ith athlete
        return [d[x] for x in score]
    
    # time complexity: O(nlog(n))
    # space complexity: O(n)
    