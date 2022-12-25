import numpy
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case
        m = len(s)
        n = len(t)
        result = ""
        if n > m:
            return result
        
        # define dict of characters in t
        t_dict = {}
        for x in t:
            t_dict.update({x:t_dict.get(x,0)+1})
        
        # define pointers
        L = 0
        R = 0
        
        # define dict of char in window that are also in t
        window_dict = {}
        for x in t:
            window_dict.update({x:0})
            
        # iterate sliding window to find minimum window substring
        while R < m:
            # add s[R] to window_dict if s[R] is in t
            if t_dict.get(s[R],0) > 0:
                window_dict.update({s[R]:window_dict.get(s[R],0)+1})
            
            # while a valid window update result
            # then shrink window and update window_dict
            valid_window = numpy.less_equal(list(t_dict.values()),list(window_dict.values())).all()
            while L <= R and valid_window:
                if len(result) > R - L + 1 or len(result) == 0:
                    result = s[L:R+1]
                if t_dict.get(s[L],0) > 0:
                    window_dict.update({s[L]:window_dict.get(s[L],0)-1})
                    valid_window = numpy.less_equal(list(t_dict.values()),list(window_dict.values())).all()
                L += 1
            
            # expand window
            R += 1
        
        # return the minimum window substring of s such that every character in t (including duplicates) is included in the window
        return result