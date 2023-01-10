class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # define longest common prefix
        common_prefix = {}
        
        i = 0
        keep_going = True
        n0 = len(strs[0])
        while keep_going:
            if i == n0:
                i += 1
                keep_going = False
                break
                
            si = strs[0][i]
            for s in strs:
                if i >= len(s) or si != s[i]:
                    keep_going = False
                    break
            i += 1
            
        return strs[0][0:i-1]