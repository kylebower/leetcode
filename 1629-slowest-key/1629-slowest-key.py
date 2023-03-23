class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # first key press
        longestTime = releaseTimes[0]
        longestKey = keysPressed[0]
        
        keyNumber = 1
        for c in keysPressed[1:]:
            curTime = releaseTimes[keyNumber] - releaseTimes[keyNumber - 1]
            if curTime >= longestTime:
                if curTime > longestTime or c > longestKey:
                    longestTime = curTime
                    longestKey = c
            keyNumber += 1
        
        return longestKey
    