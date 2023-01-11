class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # define dictionary of numbers and latest occurance
        new_dict = {}
        
        n = len(nums)
        # iterate through nums
        for i in range(n):
            if new_dict.get(nums[i],-1) != -1:
                if i - new_dict.get(nums[i]) <= k:
                    # return True if condition satisfied
                    return True
                else:
                    # update latest occurance of nums[i] in dict
                    new_dict[nums[i]] = i
            else:
                # add latest occurance of nums[i] to dict
                new_dict[nums[i]] = i
        
        # return False if no such numbers exist in nums
        return False
                    
        # time complexity: O(n)
        # space complexity: O(n)
