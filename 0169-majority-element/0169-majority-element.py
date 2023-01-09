class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # base case
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # define dict to count occurances of each number in nums
        new_dict = {}
        for i in range(n):
            new_dict.update({nums[i]:new_dict.get(nums[i],0)+1})
        new_dict_values = list(new_dict.values())
        new_dict_keys = list(new_dict.keys())
        # find index of majority element in new_dict
        for i in range(len(new_dict_keys)):
            if new_dict_values[i] > int(n/2):
                # return the majority element
                return new_dict_keys[i]
