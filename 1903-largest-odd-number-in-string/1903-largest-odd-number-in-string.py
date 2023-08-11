class Solution:
    def largestOddNumber(self, num: str) -> str:
        # find index of last odd digit
        k = len(num) - 1
        while k >= 0 and int(num[k]) % 2 == 0:
            k -= 1
        
        # Return the largest-valued odd integer
        # return "" if no odd integer exists
        return num[:k+1]
        