class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        # find digits of n
        digits = []
        while n > 0:
            digits.append(n%10)
            n = n//10
        
        # compute product and sum of digits of n
        prod_n = 1
        sum_n = 0
        for d in digits:
            prod_n *= d
            sum_n += d
        
        # return the difference between the product of its digits and the sum of its digits
        return prod_n - sum_n
