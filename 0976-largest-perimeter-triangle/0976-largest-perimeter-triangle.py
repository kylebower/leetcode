class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        # sort nums in decreasing order
        n = len(nums)
        nums.sort()
        nums = nums[::-1]
        
        # find largest perimeter of a triangle with a non-zero area
        p0 = 0
        p1 = 1
        p2 = 2
        while p2 < n:
            # if valid triangle, return perimeter
            if nums[p2] + nums[p1] > nums[p0]:
                return nums[p2] + nums[p1] + nums[p0]
            p0 += 1
            p1 += 1
            p2 += 1
        
        # If it is impossible to form any triangle of a non-zero area, return 0
        return 0
