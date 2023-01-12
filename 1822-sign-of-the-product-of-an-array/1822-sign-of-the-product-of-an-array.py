class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        
        for i in range(len(nums)):
            sign *= signFunc(nums[i])
            
        return sign

def signFunc(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0

    # time complexity: O(n)
    # space complexity: O(1)
