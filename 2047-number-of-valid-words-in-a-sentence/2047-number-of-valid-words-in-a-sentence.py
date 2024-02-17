class Solution:
    def countValidWords(self, sentence: str) -> int:
        global letters
        global digits
        global hyphens
        global punctuation
        global spaces
        letters = set()
        digits = set()
        hyphens = set()
        punctuation = set()
        spaces = set()
        
        for k in range(ord('a'), ord('z') + 1):
            letters.add(chr(k))
        for k in range(ord('0'), ord('9') + 1):
            digits.add(chr(k))
        hyphens.add('-')
        for p in ['!', '.', ',']:
            punctuation.add(p)
        spaces.add(' ')
        
        valid_words = 0
        
        words = sentence.split(" ")
        print(words)
        for w in words:
            if w == '':
                continue
            elif self.validWord(w):
                valid_words += 1
        
        return valid_words
    
    def validWord(self, word: str) -> bool:
        # return True if word is a valid word, else False
        hyphen_count = 0
        punctuation_count = 0
        
        for i, c in enumerate(word):
            if c in digits:
                return False
            elif c in hyphens:
                hyphen_count += 1
                if hyphen_count > 1:
                    return False
                if i == 0 or i == len(word)-1:
                    return False
                elif (word[i-1] not in letters) or (word[i+1] not in letters):
                    return False
            elif c in punctuation:
                punctuation_count += 1
                if punctuation_count > 1:
                    return False
                if i != len(word)-1:
                    return False
        
        return True
    