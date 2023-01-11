class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort nums
        nums.sort()
        
        # check for duplicates
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                # duplicate found
                return True
        
        # return false if no duplicates found
        return False

    # time complexity: O(nlogn)
    # space complexity: O(1)
