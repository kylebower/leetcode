class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        # check every base b between 2 and n - 2 (inclusive), 
        # the string representation of the integer n in base b is palindromic
        for b in range(2,n-1):
            # write number n in base b
            n_in_b = write_n_in_b(n,b)
            # check if number n is a palindrome in base b
            length = len(n_in_b)
            for i in range(int(length/2)):
                if n_in_b[i] != n_in_b[length-i-1]:
                    # return False if n is not a palindrome in base b
                    return False
        
        # return true if n is strictly palindromic
        return True

# define helper function to write number n in base b
# b is between 2 and n - 2 (inclusive)
def write_n_in_b(n,b):
    # find largest value of k such that b**k <= n
    k = 0
    while b**k <= n:
        k += 1
    k -= 1
    
    # find n in base b
    s = ""
    while k >= 0:
        s_to_append = n // (b**k)
        s = s + str( s_to_append )
        n = n - s_to_append * b**k
        k -= 1
    
    # return n in base b as a string
    return s