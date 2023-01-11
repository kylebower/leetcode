class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # base case:
        if n < 2:
            return 0
        
        # define left and right sums
        left_sum = 0
        right_sum = sum(nums[1:])
        middleIndex = 0
        # icrement middleIndex
        while middleIndex < n:
            # if middleIndex that satisfies the condition, return middleIndex
            if left_sum == right_sum:
                return middleIndex
            else:
                # update left and right sums
                left_sum += nums[middleIndex]
                # icrement middleIndex
                middleIndex += 1
                if middleIndex != n:
                    right_sum -= nums[middleIndex]
        
        # return -1 if there is no such index
        return -1
        