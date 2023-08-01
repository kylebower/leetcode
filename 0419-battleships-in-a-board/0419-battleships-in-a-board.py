class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # define dim of board
        m = len(board)
        n = len(board[0])
        
        # count number of cells that are the top left of a ship
        count = 0
        for mi in range(m):
            for ni in range(n):
                if board[mi][ni] == 'X' and (ni == 0 or board[mi][ni-1] != 'X') and (mi == 0 or board[mi-1][ni] != 'X'):
                    count += 1
            
        
        # return the number of the battleships on board
        return count
    