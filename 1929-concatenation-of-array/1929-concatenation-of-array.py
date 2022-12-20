class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(2*n):
            j = i % n
            result.append(nums[j])
        return result
    
    # time complexity: O(n)
    # space complexity: O(1)
