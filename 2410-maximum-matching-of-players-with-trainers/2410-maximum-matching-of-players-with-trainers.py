class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # sort players and trainers
        players.sort()
        trainers.sort()
        
        # define two pointers
        p = 0
        t = 0
        
        # iterate to match players to trainers
        matches = 0
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                matches += 1
                p += 1
                t += 1
            else:
                t += 1
        
        # Return the maximum number of matchings between players and trainers
        return matches
    