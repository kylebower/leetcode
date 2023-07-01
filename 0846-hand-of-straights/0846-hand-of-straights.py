class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        for card in sorted(c):
            cur = c[card]
            if cur > 0:
                for k in range(groupSize):
                    c[card+k] -= cur
                    if c[card+k] < 0:
                        return False
        return True
    