class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for k in range(left,right+1):
            covered = 0
            for r in ranges:
                if r[0] <= k <= r[1]:
                    covered = 1
                    break
            if covered == 0:
                return False
        return True
    