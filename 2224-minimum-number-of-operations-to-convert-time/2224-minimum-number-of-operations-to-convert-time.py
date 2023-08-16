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
        diff = correct_min - current_min
        
        # perform greedy alg to compute minimum number of operations needed to convert current to correct
        res = 0
        for i in [60, 15, 5, 1]:
            res += diff//i
            diff %= i
            
        # return Minimum Number of Operations to Convert Time
        return res
        