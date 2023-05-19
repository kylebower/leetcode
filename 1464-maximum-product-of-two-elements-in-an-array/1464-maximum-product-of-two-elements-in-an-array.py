class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        second = 0
        for n in nums:
            if n >= largest:
                second = largest
                largest = n
            elif n > second:
                second = n
        return (largest - 1) * (second - 1)
    