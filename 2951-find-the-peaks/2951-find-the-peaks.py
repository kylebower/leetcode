class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peak_indices = []
        
        for i, height in enumerate(mountain):
            if i == 0 or i == n-1:
                continue
            else:
                if height > mountain[i-1] and height > mountain[i+1]:
                    peak_indices.append(i)
        
        return peak_indices
    