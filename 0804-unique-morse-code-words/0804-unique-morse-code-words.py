class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # define array for the 26 letters of the English alphabet in Morse Code
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # make set of all transformations amoung the words we have
        set_of_transformations = set()
        for w in words:
            morse_w = ''.join([morse[ord(c)-ord('a')] for c in w])
            set_of_transformations.add(morse_w)
        
        # return the number of different transformations among all words we have
        return len(set_of_transformations)
    