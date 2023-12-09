class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        cur = arr[0]
        
        # base case
        if n < 4:
            return cur
        
        count = 1
        for i, num in enumerate(arr[1:]):
            if num == cur:
                count += 1
                if count > n/4:
                    return num
            else:
                cur = num
                count = 1
        
        return -1
    
    # time complexity: O(n)
    # space complexity: O(1)
    