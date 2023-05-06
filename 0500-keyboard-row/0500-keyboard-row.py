class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            if self.oneRow(w):
                res.append(w)
        return res
    
    def oneRow(self, w):
        d = set()
        for c in w:
            d.add(c.lower())
        firstRow = 1
        secondRow = 1
        thirdRow = 1
        for c in d:
            print(c)
            if c not in "qwertyuiop":
                firstRow = 0
            if c not in "asdfghjkl":
                secondRow = 0
            if c not in "zxcvbnm":
                thirdRow = 0
        return firstRow or secondRow or thirdRow
    