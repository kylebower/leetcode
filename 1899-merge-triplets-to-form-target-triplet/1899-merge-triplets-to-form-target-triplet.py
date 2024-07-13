class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        mergedTriplet = [0,0,0]
        
        for i in range(n):
            if max([triplets[i][j] - target[j] for j in range(3)]) <= 0:
                mergedTriplet = [max(mergedTriplet[j], triplets[i][j]) for j in range(3)]
                
        return mergedTriplet == target
    