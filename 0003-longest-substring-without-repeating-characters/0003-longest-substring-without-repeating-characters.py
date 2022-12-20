class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # base case
        n = len(s)
        if n < 2:
            return n        
        
        # define pointers
        L = 0
        R = 0
        
        # define dictionary (hash table)
        char_dict = {}
        
        # define max length
        result = 0
        
        # iterate sliding window to find longest substring
        while R < n:
            # increment s[R] by 1 in dictionary
            x = char_dict.get(s[R], 0)
            char_dict.update({s[R]:x+1})
            
            # increment L until substring has no repeats
            while len(char_dict.values()) < R-L+1:
                # increment s[L] by -1 in dictionary
                x = char_dict.get(s[L], 0)
                char_dict.update({s[L]:x-1})
                if char_dict.get(s[L], 0) == 0:
                    del char_dict[s[L]]
                L += 1
            
            # update length of the longest substring
            n_sub = R-L+1
            result = max(result, n_sub)
            
            # increment R
            R += 1
        
        # return length of the longest substring without repeating characters
        return result
