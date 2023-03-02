class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # base case
        if n == 1:
            return n
        
        players = [int(x) for x in range(1,n+1)]
        
        # eliminate players until there is only one left
        while len(players) > 1:
            players = self.elimOne(players, k)
        
        # return winner
        return players[0]
    
    def elimOne(self, players, k):
        eliminated = (k-1)%len(players)
        return players[eliminated+1:]+players[:eliminated]
    