class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        
        n_min = min(n1, n2)
        
        for k in range(n_min, 0, -1):
            substring = str1[:k]
            n_sub = len(substring)
            if str1 == ''.join([substring]*int(n1/n_sub)) and str2 == ''.join([substring]*int(n2/n_sub)):
                return substring
        
        return ''
    