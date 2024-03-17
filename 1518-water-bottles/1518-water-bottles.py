class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        bottlesDrunk = 0
        numEmptyBottles = 0
        
        while numBottles > 0:
            bottlesDrunk += numBottles
            numEmptyBottles += numBottles
            numBottles = (numEmptyBottles // numExchange)
            numEmptyBottles -= (numBottles * numExchange)
        
        return bottlesDrunk
    