class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peak_indices = []
        
        for i, height in enumerate(mountain[1:n-1]):
            if height > mountain[i] and height > mountain[i+2]:
                peak_indices.append(i+1)
        
        return peak_indices
    