class Solution:
    def equalFrequency(self, word: str) -> bool:
        # define dictionary of frequencies of each letter in word
        d = {}
        for c in word:
            d[c] = d.get(c,0) + 1
        
        # check to see if removing one letter will equalize frequency
        freq = list(d.values())
        n = len(freq)
        for i in range(n):
            freq[i] -= 1
            if freq[i] == 0:
                if min(freq[0:i] + freq[i+1:n]) == max(freq):
                    return True
            else:
                if min(freq) == max(freq):
                    return True
            freq[i] += 1
        
        return False
    