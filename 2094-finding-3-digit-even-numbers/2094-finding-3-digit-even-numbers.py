class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        d = Counter(digits)
        for k in range(100,1000,2):
            dk = Counter([int(c) for c in str(k)])
            to_append = True
            for key in list(dk.keys()):
                if dk[key] > d.get(key,0):
                    to_append = False
                    break
            if to_append:
                res.append(k)
        return res
    