class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        num_passes = tickets[k]
        time = 0
        for i in range(0,k+1):
            time += min(tickets[i], num_passes)
        for i in range(k+1,len(tickets)):
            time += min(tickets[i], num_passes-1)
        return time
            