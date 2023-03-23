class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # define length of haystack and needle
        n = len(haystack)
        m = len(needle)
        
        # define two pointers
        L = 0
        R = m
        
        # base case
        if m > n:
            return -1
        
        # iterate to find needle
        while R <= n:
            # if needle found, return index
            if haystack[L:R] == needle:
                return L
            # increment pointers
            L += 1
            R += 1
        
        # return the index of the first occurrence of needle in haystack,
        # or -1 if needle is not part of haystack
        return -1
    
    # time complexity: O(n)
    # space complexity: O(1)
    