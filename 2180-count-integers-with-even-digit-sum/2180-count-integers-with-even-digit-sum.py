class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for k in range(1,num+1):
            if self.digitSum(k)%2 == 0:
                res += 1
        return res
    
    def digitSum(self, k: int) -> int:
        # return sum of all digits in k
        digit_sum = 0
        while k > 0:
            last_digit = k%10
            digit_sum += last_digit
            k //= 10
        return digit_sum
            