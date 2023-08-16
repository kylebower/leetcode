class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # record minutes and hours
        MM = int(current[3:])
        HH = int(current[:2])
        mm = int(correct[3:])
        hh = int(correct[:2])
        
        # convert time to minutes
        correct_min = 60*hh + mm
        current_min = 60*HH + MM
        
        # perform greedy alg to compute minimum number of operations needed to convert current to correct
        res = 0
        while (correct_min - current_min) % (60*24) >= 60:
            current_min = (current_min + 60) % (60*24)
            res += 1
        while (correct_min - current_min) % (60*24) >= 15:
            current_min = (current_min + 15) % (60*24)
            res += 1
        while (correct_min - current_min) % (60*24) >= 5:
            current_min = (current_min + 5) % (60*24)
            res += 1
        while (correct_min - current_min) % (60*24) >= 1:
            current_min = (current_min + 1) % (60*24)
            res += 1
        
        # return Minimum Number of Operations to Convert Time
        return res
        