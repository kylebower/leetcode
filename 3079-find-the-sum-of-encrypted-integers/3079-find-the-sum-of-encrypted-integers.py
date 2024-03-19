class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += self.encrypt(num)
        return res
    
    def encrypt(self, x: int) -> int:
        # replaces every digit in x with the largest digit in x
        max_digit = 0
        for c in str(x):
            if int(c) > max_digit:
                max_digit = int(c)
        return int(''.join([str(max_digit)]*len(str(x))))
    