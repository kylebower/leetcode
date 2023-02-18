class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.isPalindrome(w):
                return w
        
        return ''
    
    def isPalindrome(self, w):
        n = len(w)
        for i in range(int(n/2)):
            if w[i] != w[n-i-1]:
                return False
        return True
    