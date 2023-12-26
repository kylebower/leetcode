class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        for rect in rectangles:
            maxLen = max(maxLen, min(rect))
        number = 0
        for rect in rectangles:
            if min(rect) == maxLen:
                number += 1
        return number
    