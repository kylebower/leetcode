class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first_letters = ''.join([w[0] for w in words])
        return first_letters == s
    