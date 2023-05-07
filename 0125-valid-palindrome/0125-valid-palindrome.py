class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean data
        # converting all uppercase letters into lowercase letters
        s = s.lower()
        # removing all non-alphanumeric characters
        s = self.removeNonAlpha(s)
        
        # use two pointers
        n = len(s)
        L = 0
        R = n-1
        while L < R:
            # return False if not a palindrome
            if s[L] != s[R]:
                return False
            # move pointers to check next letters
            L += 1
            R -= 1
            
        # return True if palindrome
        return True
    
    def removeNonAlpha(self, s: str) -> str:
        res = []
        for c in s:
            ordc = ord(c)
            if (ordc >= ord('a') and ordc <= ord('z')) or (ordc >= ord('0') and ordc <= ord('9')):
                res.append(c)
        return ''.join(res)        
        