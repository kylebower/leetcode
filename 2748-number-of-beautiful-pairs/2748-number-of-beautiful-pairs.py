class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        num_beautiful_pairs = 0
        n = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if self.isBeautifulPair(nums[i], nums[j]):
                    num_beautiful_pairs += 1
        return num_beautiful_pairs
    
    def isBeautifulPair(self, a: int, b: int) -> bool:
        # return True if a and b form a beautiful pair
        # otherwise return false
        a_first = int(str(a)[0])
        b_last = int(str(b)[-1])
        return self.gcd(a_first, b_last) == 1
    
    def gcd(self, x: int, y: int) -> int:
        # return greatest common divisor of x and y
        gcd = 1
        for k in range(2,min(x,y)+1):
            if (x%k == 0) and (y%k == 0):
                gcd = k
        return gcd
    