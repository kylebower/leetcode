class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        
        counts = collections.Counter(tasks)
        
        for difficulty in counts:
            tasks = counts[difficulty]
            if tasks == 1:
                return -1
            else:
                rounds += math.ceil(tasks/3)
        
        return rounds
    