class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = dic.get(c,0) + 1
        
        dic_values = list(dic.values())
        dic_values2 = [x//2 for x in dic_values]
        
        if [x*2 for x in dic_values2] == dic_values:
            longest = 2*sum(dic_values2)
        else:
            longest = 2*sum(dic_values2) + 1
        
        return longest
        
        # time complexity: O(n)
        # space complexity: O(n)
