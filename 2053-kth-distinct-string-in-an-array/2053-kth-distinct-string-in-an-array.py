class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # define dict of occurences of srings in arr
        d = {}
        
        # add each string to dict
        for s in arr:
            d[s] = d.get(s,0) + 1
        
        # find kth distinct string
        num_distinct = 0
        for s in d:
            if d[s] == 1:
                num_distinct += 1
                if num_distinct == k:
                    return s
        
        #  If there are fewer than k distinct strings, return an empty string
        return ''
    