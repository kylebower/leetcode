class Solution:
    def largestInteger(self, num: int) -> int:
        nums_odd = [int(x) for x in str(num) if int(x)%2==1]
        nums_even = [int(x) for x in str(num) if int(x)%2==0]
        nums_odd.sort(key = lambda x: -x)
        nums_even.sort(key = lambda x: -x)
        
        parity = [int(x)%2 for x in str(num)]
        nums = [int(x) for x in str(num)]
        
        res = [0]*len(nums)
        i = 0   # odd counter
        j = 0   # even counter
        k = 0   # counter
        while k < len(nums):
            if parity[k]: # odd
                res[k] = nums_odd[i]
                i += 1
            else:
                res[k] = nums_even[j]
                j += 1
            k += 1
        
        res_str = [str(x) for x in res]
        return int(''.join(res_str))
    