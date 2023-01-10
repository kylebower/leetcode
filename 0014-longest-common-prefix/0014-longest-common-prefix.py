class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # find shortest string in strs
        shortest = min(strs,key=len)
        
        # for each char in shortest
        for i, ch in enumerate(shortest):
            # for each other string
            for other in strs:
                # test for prefix
                if other[i] != ch:
                    return shortest[:i]
        
        # return entire string shortest if it is a prefix for all other strings
        return shortest
