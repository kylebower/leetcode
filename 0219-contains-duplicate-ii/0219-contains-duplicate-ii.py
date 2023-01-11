class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # define dictionary of numbers and latest occurance
        dic = {}
        
        # iterate through nums
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                # return True if condition satisfied
                return True
            else:
                # add latest occurance of nums[i] to dict
                dic[v] = i
        
        # return False if no such numbers exist in nums
        return False
                    
        # time complexity: O(n)
        # space complexity: O(n)
