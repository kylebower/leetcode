class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        # define dict for value of each char
        d = {}
        for i in range(26):
            d[chr(ord('a')+i)] = i+1
        for i,c in enumerate(chars):
            d[c] = vals[i]
        
        # compute maximal cost of substring ending at each position
        res = 0
        cur = 0
        for i in range(len(s)):
            cur = cur + d[s[i]]
            # store maximal cost seen so far
            res = max(cur,res)
            if cur < 0:
                cur = 0
        
        # return maximal cost of substring
        return res
    
    # time complexity: O(n)
    # space complexity: O(1)
        