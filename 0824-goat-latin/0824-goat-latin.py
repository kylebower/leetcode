class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # define vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        # split sentence into words
        words = sentence.split(' ')
        
        # convert words to Goat Latin
        for i,w in enumerate(words):
            if w[0].lower() in vowels:
                words[i] = w + 'ma' + 'a'*(i+1)
            else:
                words[i] = w[1:] + w[0] + 'ma' + 'a'*(i+1)
        
        # Return the final sentence
        return ' '.join(words)
        