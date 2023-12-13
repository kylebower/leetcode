class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [words[0]] + [w for i, w in enumerate(words[1:]) if Counter(w) != Counter(words[i])]