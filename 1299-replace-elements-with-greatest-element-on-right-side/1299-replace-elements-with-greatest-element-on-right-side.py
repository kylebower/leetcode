class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        n = len(arr)
        for i in range(n):
            cur = arr[n-1-i]
            arr[n-1-i] = greatest
            greatest = max(greatest, cur)
        return arr
    