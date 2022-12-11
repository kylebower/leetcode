class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = nums
        if len(result) == 1:
            return result
        else:
            for i in range(1,len(result)):
                result[i] += result[i-1]
            return result
            