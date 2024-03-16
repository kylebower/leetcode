class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        cur_sum = 0
        
        cur_sum += min(k, numOnes)
        k -= min(k, numOnes)        
        
        k -= min(k, numZeros)        
        
        cur_sum -= min(k, numNegOnes)
        k -= min(k, numNegOnes)
        
        return cur_sum
    