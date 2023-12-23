class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        k = 0
        nums = []        
        res = []
        
        for i, w in enumerate(words):
            if w == 'prev':
                k += 1
                if k > len(nums):
                    res.append(-1)
                else:
                    res.append(nums[-k])
            else:
                k = 0
                nums.append(int(w))
        
        return res
    