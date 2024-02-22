class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        num_symmetric = 0
        
        for k in range(low, high + 1):
            if self.isSymmetric(str(k)):
                num_symmetric += 1
        
        return num_symmetric
    
    def isSymmetric(self, k: str) -> bool:
        # return True if k is symmetric, else False
        m = len(k)
        sum_first_half = 0
        sum_second_half = 0
        if len(k)%2 == 1:
            return False
        else:
            for i in range(m//2):
                sum_first_half += int(k[i])
                sum_second_half += int(k[i+m//2])
            return sum_first_half == sum_second_half
        