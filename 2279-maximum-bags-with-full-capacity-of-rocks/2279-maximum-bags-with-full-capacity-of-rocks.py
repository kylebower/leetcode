class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # update capacity to be extra space available
        for i, cap in enumerate(capacity):
            capacity[i] = cap - rocks[i]
        
        # sort capacity
        capacity.sort()
        
        # count Maximum Bags With Full Capacity of Rocks
        count = 0
        k = 0
        while k < len(capacity) and (additionalRocks > 0 or capacity[k] == 0):
            additionalRocks -= capacity[k]
            k += 1            
            count += 1
        if additionalRocks < 0:
            count -= 1
        
        # return count
        return count
    