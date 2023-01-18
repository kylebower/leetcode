class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = set()
        for c in s:
            if c in letters:
                return c
            else:
                letters.add(c)
