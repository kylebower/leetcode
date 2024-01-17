class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for _ in range(k):
            gifts.sort(reverse = True)
            gifts[0] = floor(sqrt(gifts[0]))
        
        return sum(gifts)
                