class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for k in range(1, len(pref)):
            arr.append(pref[k-1]^pref[k])
        return arr
    