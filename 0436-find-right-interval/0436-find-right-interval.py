class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # make dict d[starti] = i
        d = {}
        for i, interval in enumerate(intervals):
            d[interval[0]] = i
        
        # sort start times
        start = [x[0] for x in intervals]
        start.sort()
        
        n = len(intervals)
        res = [-1]*n
        for i, interval in enumerate(intervals):
            endi = interval[1]
            j = self.binarySearch(start, endi)
            if j == -1:
                res[i] == -1
            else:
                startj = start[j]
                res[i] = d[startj]
        
        return res
    
    def binarySearch(self, times: List[int], target: int) -> int:
        # find smallest time >= target
        n = len(times)
        L = 0
        R = n-1
        while L + 1 < R:
            mid = int(L + (R-L)/2)
            cur = times[mid]
            if cur == target:
                return mid
            elif cur > target:
                R = mid
            else:  # cur < target
                L = mid
        if times[L] >= target:
            return L
        elif times[R] >= target:
            return R
        else:
            return -1
        