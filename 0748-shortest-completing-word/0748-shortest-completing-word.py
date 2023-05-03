class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # define dict of all char in licensePlate
        d_lp = {}
        for c in licensePlate:
            if self.isLetter(c):
                cur = c.lower()
                d_lp[cur] = d_lp.get(cur,0)+1
        # define length of shortest completing word
        shortest_length = math.inf
        
        # iterate through words to find shortest completing word
        for w in words:
            if len(w)<shortest_length and self.completing(w,d_lp):
                shortest = w
                shortest_length = len(w)
                
        # return shortest completing word
        return shortest
    
    def completing(self, w: str, d_lp: dict) -> bool:
        # return True if w is a completing word, else False
        d_w = {}
        for c in w:
            d_w[c] = d_w.get(c,0)+1
        for key in d_lp:
            if d_lp[key] > d_w.get(key,0):
                return False
        return True
    
    def isLetter(self, c: str) -> bool:
        # return True if c is a letter, else False
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            return True
        elif (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            return True
        else:
            return False
        