class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        # define length of nums and queries
        n = len(nums)
        m = len(queries)
        
        # define answer array
        answer = [0]*m
        
        # sort nums
        nums.sort()
        
        # define sum so far of nums
        sumSoFar = nums
        for i in range(1,n):
            sumSoFar[i] += sumSoFar[i-1]
        # iterate to update answer array
        for i in range(m):
            answer[i] = self.getMaxSub(sumSoFar, queries[i])        
        
        # return array answer of length m where answer[i] is the maximum size 
        # of a subsequence that you can take from nums such that the sum of its 
        # elements is less than or equal to queries[i]
        return answer
    
    def getMaxSub(self, sumSoFar, q):
        # return maximum size of a subsequence of nums such that the sum of its 
        # elements is less than or equal to q
        
        # define two pointers
        L = 0
        R = len(sumSoFar)-1
        
        # perform binary search to find largest index i such that sumSoFar[i] < q
        while L+1 < R:
            mid = int(L + (R-L)/2)
            cur = sumSoFar[mid]
            if cur == q:
                return mid+1
            elif cur < q:
                L = mid
            else:  # cur > q
                R = mid-1 
        # return result
        if sumSoFar[R] <= q:
            return R+1
        elif sumSoFar[L] <= q:
            return L+1
        else:
            return L
        