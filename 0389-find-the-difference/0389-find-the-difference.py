class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        c = 0
        for cs in s:
            c ^= ord(cs)  #ord is ASCII value
        
        for ct in t:
            c ^= ord(ct)
        
        return chr(c) # convert from ASCII to string

    # time complexity: O(n)
    # space complexity: O(1)
