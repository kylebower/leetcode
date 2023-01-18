class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        # reverse num to get reversed1
        num1 = num
        reversed1 = 0
        while num1 > 0:
            reversed1 *= 10
            reversed1 += num1%10
            num1 //= 10
        
        # reverse reversed1 to get reversed2
        reversed2 = 0
        while reversed1 > 0:
            reversed2 *= 10
            reversed2 += reversed1%10
            reversed1 //= 10
        
        # Return true if reversed2 equals num. Otherwise return false
        return reversed2 == num