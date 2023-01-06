class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # return false if x is negative
        if x < 0:
            return False

        # write reverse of input number        
        input_number = x
        reversed_number = 0
        while x > 0:
            reversed_number = reversed_number * 10 + x % 10
            x = x // 10
            
        # return true if x is a palindrome, and false otherwise.
        return reversed_number == input_number
