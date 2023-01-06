class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        x_length = len(x_string)
        
        # base case
        if x_length <= 1:
            return True
        
        # check if x is a palindrome
        for i in range(x_length):
            if x_string[i] != x_string[x_length-1-i]:
                # return false if x is not a palindrome
                return False
        # return true if x is a palindrome
        return True
