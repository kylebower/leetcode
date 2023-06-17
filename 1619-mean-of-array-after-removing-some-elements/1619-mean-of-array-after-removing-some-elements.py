class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        return sum(arr[int(.05*n):int(.95*n)]) / (.9*n)
    