class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        noninc = True
        nondec = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nondec = False
            elif nums[i] < nums[i+1]:
                noninc = False
        return noninc or nondec
    
    # time complexity: O(n)
    # space complexity: O(1)
    