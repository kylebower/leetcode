class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        sumOdd = 0
        for i in range(n):
            sumOdd += arr[i]*self.numOddArrays(i,n)
        return sumOdd
            
    def numOddArrays(self, i: int, n: int) -> int:
        return int(((i+1)*(n-i)+1)/2)
