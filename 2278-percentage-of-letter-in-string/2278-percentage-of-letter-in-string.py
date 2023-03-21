class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = 0
        count = 0
        for c in s:
            n += 1
            if c == letter:
                count += 1
        return int(count/n*100)
    