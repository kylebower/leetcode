class Solution:
    def reverseWords(self, s: str) -> str:
        
        # split s
        words = s.split()
        
        # reverse order words
        n = len(words)
        for i in range(int(n/2)):
            temp = words[i]
            words[i] = words[n-1-i]
            words[n-1-i] = temp
        
        # return new string
        return ' '.join(words)
    