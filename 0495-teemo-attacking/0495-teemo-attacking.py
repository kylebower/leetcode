class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        atkUntil = -inf
        res = 0
        for t in timeSeries:
            if t >= atkUntil:
                res += duration
            else:
                res += t + duration - atkUntil
            atkUntil = t + duration
        return res
    