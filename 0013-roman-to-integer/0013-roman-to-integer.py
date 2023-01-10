class Solution:
    def romanToInt(self, s: str) -> int:
        
        # define integer number
        num = 0
        
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            if c == "M":
                num += 1000
            elif c == "D":
                num += 500
            elif c == "C":
                if i == n-1 or (s[i+1] != "D" and s[i+1] != "M"):
                    num += 100
                elif s[i+1] == "D":
                    num += 400
                    i += 1
                elif s[i+1] == "M":
                    num += 900
                    i += 1
            elif c == "L":
                num += 50
            elif c == "X":
                if i == n-1 or (s[i+1] != "L" and s[i+1] != "C"):
                    num += 10
                elif s[i+1] == "L":
                    num += 40
                    i += 1
                elif s[i+1] == "C":
                    num += 90
                    i += 1
            elif c == "V":
                num += 5
            elif c == "I":
                if i == n-1 or (s[i+1] != "V" and s[i+1] != "X"):
                    num += 1
                elif s[i+1] == "V":
                    num += 4
                    i += 1
                elif s[i+1] == "X":
                    num += 9
                    i += 1
            i += 1
        return num
            
        