class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # make dict of indices of each char in s
        d = {}
        for i,c in enumerate(s):
            if c not in d:
                d[c] = [i]
            else:
                d[c] = d[c] + [i]
        
        # return -1 if no repeated char in s
        if max([len(x) for x in list(d.values())]) < 2:
            return -1
        
        # return the length of the longest substring between two equal characters, excluding the two characters
        lengths = [x[-1] - x[0] - 1 for x in list(d.values())]
        return max(lengths)
    