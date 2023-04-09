class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        # define two pointers
        L = 0
        n = len(colors)
        R = n-1
        
        # base case
        if colors[n-1] != colors[0]:
            return n-1
        
        # increment left pointer, until we get to a house of a different color
        while colors[L] == colors[0]:
            L += 1
        
        # decrement right pointer until we get to a house of a different color
        while colors[R] == colors[n-1]:
            R -= 1
        
        # return max distance between two houses with different colors
        return max(n-1-L, R)
    