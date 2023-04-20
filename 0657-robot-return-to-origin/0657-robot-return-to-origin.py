class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # define dict of robots moves
        d = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for m in moves:
            d[m] = d.get(m) + 1
        
        # check that robot end up at origin
        return d['L'] == d['R'] and d['U'] == d['D']
        