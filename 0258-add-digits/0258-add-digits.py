class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = add_digits(num)
        return num
    
def add_digits(n):
    new_num = 0
    while n > 0:
        d = n%10
        new_num += d
        n = n // 10
    return new_num
