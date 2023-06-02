class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # define output array
        res = [0]*len(deck)
        
        # sort deck in descending order
        deck.sort(reverse=1)
        
        # fill output array
        insert = 1
        while deck:
            for i,_ in enumerate(res):
                if res[i] != 0:
                    continue
                elif insert:
                    res[i] = deck.pop()
                    insert = 0
                else:
                    insert = 1
        
        # return ordering of the deck that would reveal the cards in increasing order
        return res