class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # base case:
        # return false if hand can not be rearranged into groups of size groupSize
        n = len(hand)
        if n%groupSize != 0:
            return False
        
        # sort hand
        hand.sort()
        
        # make dict of occurences of each card in hand
        d = {}
        for card in hand:
            d[card] = d.get(card,0) + 1
            
        # rearrange the cards into groups of straights
        while len(d) > 0:
            start = min(list(d.keys()))
            for k in range(groupSize):
                if start+k not in d:
                    return False
                else:
                    d[start+k] = d.get(start+k)-1
                    if d[start+k] == 0:
                        del d[start+k]
        
        # return True if she can rearrange the cards
        return True
    