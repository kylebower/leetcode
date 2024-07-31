class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        
        while mainTank > 0:
            fuelUsed = min(5, mainTank)
            mainTank -= fuelUsed
            if fuelUsed == 5 and additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
            distance += 10 * fuelUsed
        
        return distance
    