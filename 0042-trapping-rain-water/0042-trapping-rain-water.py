class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # Base case
        if n < 3:
            return 0        
        
        # find index of maximal height
        max_index = 0
        for i in range(n):
            if height[i] > height[max_index]:
                max_index = i        
        
        rain_trapped = 0
        # find trapped water to the left of max index
        left_max = 0
        for i in range(max_index):
            if height[i] > left_max:
                left_max = height[i]
            rain_trapped += left_max - height[i]
        
        # find trapped water to the right of max index
        right_max = 0
        for i in range(n-1, max_index, -1):
            if height[i] > right_max:
                right_max = height[i]
            rain_trapped += right_max - height[i]
            
        return rain_trapped