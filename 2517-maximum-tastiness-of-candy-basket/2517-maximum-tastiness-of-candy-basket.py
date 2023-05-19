class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # use binary search to find max tastiness of a candy basket
        
        # define two pointers for bounds on step size
        L = 0
        R = max(price)
        
        # sort prices
        price.sort()
        
        # perform binary search
        while L+1 < R:
            mid = int(L+(R-L)/2)
            if self.possible(price, mid, k):
                L = mid
            else:
                R = mid
        if self.possible(price, R, k):
            return R
        else:
            return L
        
    def possible(self, price: List[int], stepSize: int, k: int) -> bool:
        count = 0
        cur = 0
        for p in price:
            if p >= cur:
                count += 1
                cur = p + stepSize
        return count >= k 
        
    # time complexity: O(nlog(n))
    # space complexity: O(1)
    