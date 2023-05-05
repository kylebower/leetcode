class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.": paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower()
        words = paragraph.split()
        d = {}
        for w in words:
            if w not in banned:
                d[w] = d.get(w,0)+1
        most_freq = 0
        res = ""
        for w in d:
            if d[w] >= most_freq:
                res = w
                most_freq = d[w]
        return res
    