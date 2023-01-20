class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # base case
        if len(words) < 2:
            return True
        
        # define alien dictionary
        alien_dict = {}
        i = 0
        for c in order:
            alien_dict[c] = i
            i += 1
        
        # translate alien words into number
        new_words = []
        for w in words:
            new_word = []
            for ch in w:
                new_word.append(alien_dict[ch])
            new_words.append(new_word)
        
        # return false if any two words are out of order
        for w1, w2 in zip(new_words, new_words[1:]):
            if w2 < w1:
                return False
        
        # return True if words are sorted lexicographically in this alien language
        return True
        