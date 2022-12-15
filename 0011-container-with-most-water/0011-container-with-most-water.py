class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        # Base case
        if n < 2:
            return 0
        
        # define pointers
        L = 0
        R = n - 1
        maxVolumeSoFar = (R-L)*min(height[L], height[R])
        
        while R > L+1:            
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
            newVolume = (R-L)*min(height[L], height[R])
            maxVolumeSoFar = max(maxVolumeSoFar, newVolume)
        return maxVolumeSoFar