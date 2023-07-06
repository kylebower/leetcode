class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = None
        max2 = None
        max3 = None
        
        for n in nums:
            if n == max1 or n == max2 or n == max3:
                continue
            elif max1 == None or n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif max2 == None or n > max2:
                max3 = max2
                max2 = n
            elif max3 == None or n > max3:
                max3 = n
        
        return max1 if max3 == None else max3
        
    # time complexity: O(n)
    # space complexity: O(1)
    