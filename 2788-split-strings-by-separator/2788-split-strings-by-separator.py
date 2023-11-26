class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for w in words:
            split = w.split(separator)
            for word in split:
                if word != "":
                    res.append(word)
        return res
    