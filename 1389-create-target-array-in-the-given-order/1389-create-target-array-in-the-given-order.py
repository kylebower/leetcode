class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        # define empty target array
        target = []
        
        # insert at index index[i] the value nums[i] in target array
        for i in range(len(nums)):
            target = target[:index[i]] + [nums[i]] + target[index[i]:]
        
        # Return the target array
        return target
        