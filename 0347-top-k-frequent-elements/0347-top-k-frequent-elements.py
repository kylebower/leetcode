class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make dict of occurences
        d = {}
        for n in nums:
            d[n] = d.get(n,0)+1
        
        # sort list of numbers by occurences
        numbers = list(d.keys())
        numbers = sorted(numbers, key = lambda x: d[x])[::-1]
        
        # return the k most frequent elements
        return numbers[:k]
        