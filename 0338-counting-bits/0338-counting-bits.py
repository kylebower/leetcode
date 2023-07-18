class Solution:
    def countBits(self, n: int) -> List[int]:
        # dynamic programming solution
        
        # define answer array
        ans = [0]*(n+1)
        
        # iterate for each i, (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i
        offset = 1
        for i in range(1,n+1):
            if i == 2*offset:
                offset = i
            ans[i] = ans[i-offset] + 1
        
        # return answer array
        return ans
    