class Solution:
    def reverseWords(self, s: str) -> str:
        # convert to list of char
        s = list(s)
        
        # define length of string
        n = len(s)
        
        # define two pointers
        L = 0
        R = 1
        
        # increment two pointers to find words
        while R < n:
            if s[R] == ' ':
                # reverse order of each word
                s = self.reverse(s,L,R-1)
                L = R+1
                R = L+1
            else:
                R += 1
        # reverse order of last word        
        s = self.reverse(s,L,R-1)
        
        # return str with each word reversed
        return ''.join(s)
        
    def reverse(self, s, L, R):
        word = s[L:R+1]
        n = len(word)
        for i in range(int(n/2)):
            temp = word[i]
            word[i] = word[n-1-i]
            word[n-1-i] = temp
        return s[:L] + word + s[R+1:]
