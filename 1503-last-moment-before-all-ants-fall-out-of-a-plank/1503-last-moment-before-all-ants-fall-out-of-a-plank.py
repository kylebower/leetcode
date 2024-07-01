class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max([n-x for x in right] + [x for x in left])