class Solution:
    def isHappy(self, n: int) -> bool:
        # base case
        if n == 1:
            return True
        
        prev_n = []
        
        while n > 1:
            n = sum_of_squares_of_digits(n)
            if n == 1:
                return True
            elif n in prev_n:
                return False
            else:
                prev_n.append(n)

def sum_of_squares_of_digits(n):
    new_num = 0
    while n > 0:
        d = n%10
        new_num += d*d
        n = n // 10
    return new_num
