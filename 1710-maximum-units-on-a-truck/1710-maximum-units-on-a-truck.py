class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        bu = [[x[1],x[0]] for x in boxTypes]
        bu.sort()
        bu = bu[::-1]
        print(bu)
        
        space_used = 0
        units = 0
        boxNum = 0
        while space_used < truckSize and boxNum < len(boxTypes):
            space = min(truckSize-space_used, bu[boxNum][1])
            space_used += space
            units += space*bu[boxNum][0]
            boxNum += 1
        
        return units
    