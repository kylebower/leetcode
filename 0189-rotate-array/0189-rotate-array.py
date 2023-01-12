class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # base case
        k = k%n
        if k == 0 or n == 1:
            return
        
        # 3-step array rotation
        # reverse first n-k elements
        self.reverse(nums,0,n-k-1)
        # reverse last k elements
        self.reverse(nums,n-k,n-1)
        # reverse entire array
        self.reverse(nums,0,n-1)

    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
