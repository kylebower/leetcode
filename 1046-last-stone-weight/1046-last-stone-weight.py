class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            if stones[0] == stones[1]:
                stones = stones[2:]
            else:
                stones = [stones[0] - stones[1]] + stones[2:]
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
    