class Solution:
    def romanToInt(self, s: str) -> int:
        
        # define dict for roman numerals
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        # define int to return
        num = 0
        
        # define length of string s
        n = len(s)
        
        # construct int to return
        for i in range(n-1):
            # if next char corresponds to greater roman numeral, then subtract value
            if roman_dict[s[i+1]] > roman_dict[s[i]]:
                num -= roman_dict[s[i]]
            else:
                # add value
                num += roman_dict[s[i]]
        
        # add final value
        num += roman_dict[s[n-1]]
        
        # return int
        return num
