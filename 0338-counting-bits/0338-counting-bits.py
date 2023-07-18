class Solution:
    def countBits(self, n: int) -> List[int]:
        # define answer array
        ans = [0]*(n+1)
        
        # iterate for each i, (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i
        for i in range(n+1):
            ans[i] = self.getOnes(i)
        
        # return answer array
        return ans
    
    def getOnes(self, k: int) -> int:
        res = 0
        while k > 0:
            res += k%2
            k //= 2
        return res
    