class Solution:
    def sortSentence(self, s: str) -> str:
        # split s into list of strings
        s = s.split()
        
        # s1 is a list of words
        # s2 is a list of the 1-indexed word position
        s1 = []
        s2 = []
        for i in range(len(s)):
            s1.append(s[i][:-1])
            s2.append(s[i][-1])
        
        # sort the words
        s3 = [x for _,x in sorted(zip(s2,s1))]
        
        # return the original sentence
        return " ".join(s3)
