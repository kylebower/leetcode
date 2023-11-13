class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # define number of available captures
        num_captures = 0
        
        # find location of rook
        rx = 0
        ry = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rx = i
                    ry = j
                    break
        
        # check capture to left
        for i in range(rx, -1, -1):
            if board[i][ry] == 'B':
                break
            elif board[i][ry] == 'p':
                num_captures += 1
                break
        
        # check capture to right
        for i in range(rx, 8):
            if board[i][ry] == 'B':
                break
            elif board[i][ry] == 'p':
                num_captures += 1
                break
        
        # check capture up
        for i in range(ry, -1, -1):
            if board[rx][i] == 'B':
                break
            elif board[rx][i] == 'p':
                num_captures += 1
                break
        
        # check capture down
        for i in range(ry, 8):
            if board[rx][i] == 'B':
                break
            elif board[rx][i] == 'p':
                num_captures += 1
                break
        
        # return number of available captures
        return num_captures
    