class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # define new string
        new_string = ""
        
        while word1 and word2:
            # add letters in alternating order to new string
            new_string += word1[0]
            new_string += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        
        # append additional letters to merged string
        if word1:
            new_string += word1
        elif word2:
            new_string += word2
        
        # return merged string
        return new_string
