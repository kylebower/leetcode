class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: -x[1])
        
        res = 0
        for boxes, units in boxTypes:
            if boxes < truckSize:
                truckSize -= boxes
                res += units*boxes
            else:
                res += units*truckSize
                return res
            
        return res
    