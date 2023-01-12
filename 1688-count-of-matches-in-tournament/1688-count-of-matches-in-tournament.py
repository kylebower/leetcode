class Solution:
    def numberOfMatches(self, n: int) -> int:
        # n is the number of teams left in the tournament
        
        # define number of matches played
        num_matches = 0
        
        # play until a winner is decided
        while n > 1:
            if n%2 == 0: # current number of teams is even
                num_matches += int(n / 2)
                n /= 2
            else: # current number of teams is odd
                num_matches += int((n - 1) / 2)
                n = (n - 1) / 2 + 1
                
        # Return the number of matches played in the tournament        
        return num_matches
