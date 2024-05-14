class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == 'O':
                i += 1
            if i < len(s) and s[i] == 'X':
                i += 3
                moves += 1
        return moves
    