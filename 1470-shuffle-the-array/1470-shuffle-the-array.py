class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        result = [None]*n
        for i in range(n):
            if i % 2 == 0:
                result[i] = nums[int(i/2)]
            else:
                result[i] = nums[int((i-1)/2+n/2)]
        return result
    
    # time complexity: O(n)
    # space complexity: O(1)
