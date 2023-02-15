class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # base case
        if len(nums) < 2:
            return len(nums)
        
        # sort nums
        nums.sort()
        
        # remove duplicates
        old = nums
        new_nums = []
        new_nums.append(old[0])
        
        for i in range(1,len(nums)):
            if old[i] != old[i-1]:
                new_nums.append(old[i])
        
        # define counter for current sequence and longest ever
        curr = 1
        longest = 1
        for i in range(1,len(new_nums)):
            if new_nums[i] == new_nums[i-1]+1:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1
        
        return longest
        