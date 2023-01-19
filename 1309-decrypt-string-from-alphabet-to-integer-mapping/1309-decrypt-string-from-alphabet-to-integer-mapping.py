class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic1 = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i'}
        dic2 = {'10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
        
        for c in list(dic2.keys()):
            s = s.replace(c,dic2[c])
        for c in list(dic1.keys()):
            s = s.replace(c,dic1[c])
        
        return s