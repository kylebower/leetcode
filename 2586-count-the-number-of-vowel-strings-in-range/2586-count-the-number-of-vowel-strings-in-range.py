class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        res = 0
        for k in range(left, right+1):
            if self.isVowelString(words[k]):
                res += 1
        return res
    
    def isVowelString(self, w: str):
        vowels = ['a', 'e', 'i', 'o', 'u']
        return w[0] in vowels and w[-1] in vowels
    