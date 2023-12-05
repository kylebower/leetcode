class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = {}
        for w in words:
            letters = [c for c in set(w)]
            letters.sort()
            word = ''.join(letters)
            d[word] = d.get(word,0)+1
        res = 0
        for k in list(d.values()):
            res += k*(k-1)/2
        return int(res)
    