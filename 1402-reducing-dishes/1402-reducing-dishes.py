class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        # sort dishes by satisfaction
        satisfaction.sort(reverse=1)
        
        # sum of satisfaction so far
        sumSoFar = 0
        
        # current satisfaction
        cur = 0
        
        # maximum sum of like-time coefficient
        best = 0
        
        # iterate to find maximum sum of like-time coefficient
        for _, dish in enumerate(satisfaction):
            cur += sumSoFar + dish
            sumSoFar += dish
            best = max(cur,best)
        
        # return maximum sum of like-time coefficient
        return best
        