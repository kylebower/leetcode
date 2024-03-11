class Solution:
    def minimumPushes(self, word: str) -> int:
        d = collections.Counter(word)
        frequencies = sorted(list(d.values()), reverse=True)
        
        presses = 0
        for i, freq in enumerate(frequencies):
            presses += freq * (i // 8 + 1)
        
        return presses
    