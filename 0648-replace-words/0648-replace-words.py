class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # sort dicttionary by shortest length
        dictionary.sort()
        
        # for each word that is a successor in sentence, replace by shortest root
        words = sentence.split(' ')
        for i,word in enumerate(words):
            for dict_word in dictionary:
                if len(dict_word) <= len(word) and dict_word == word[:len(dict_word)]:
                    words[i] = dict_word
                    break
        
        # Return the sentence after the replacement.
        return ' '.join(words)
        