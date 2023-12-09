class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)        
        count = 0
        cur = inf
        
        for num in arr:
            if num == cur:
                count += 1
            else:
                cur = num
                count = 1
            if count > n/4:
                return num
        
        return -1
    
    # time complexity: O(n)
    # space complexity: O(1)
    