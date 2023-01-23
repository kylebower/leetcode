class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        sorted_arr = [0]*len(arr)
        arr.sort()
        
        num_bits = [0]*len(arr)
        for i,val in enumerate(arr):
            num_bits[i] = self.nums_one_bits(val)
        
        sorted_arr = [y for x,y in sorted(zip(num_bits,arr))]
        
        return sorted_arr
    
    def nums_one_bits(self, val):
        res = 0
        while val > 0:
            res += val%2
            val //= 2
        return res
            