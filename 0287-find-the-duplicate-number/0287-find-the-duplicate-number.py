class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # base case
        n = len(nums)
        if n < 3:
            return nums[0]
        
        # define fast and slow pointers
        fast = nums[nums[0]]
        slow = nums[0]
        
        # traverse the array to find a cycle
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
        # perform Floyd's alg to find first node in cycle
        p1 = 0
        p2 = fast
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
            
        # return the repeated number
        return p1