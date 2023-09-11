class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first_letters = ''
        for w in words:
            first_letters += w[0]
        return first_letters == s
    