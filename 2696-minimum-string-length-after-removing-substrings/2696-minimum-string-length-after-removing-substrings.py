class Solution:
    def minLength(self, s: str) -> int:
        foundPair = True
        while foundPair:
            foundPair = False
            for i in range(len(s) - 1):
                if s[i:i+2] == 'AB' or s[i:i+2] == 'CD':
                    s = s[:i] + s[i+2:]
                    foundPair = True
        return len(s)
    