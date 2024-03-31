class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # base case
        if num < 6:
            return False
        
        divisor_sum = 1
        for k in range(2, math.floor(sqrt(num)) + 1):
            if num%k == 0:
                divisor_sum += k + num//k
        
        return divisor_sum == num
    