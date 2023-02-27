class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # define output array
        res = [0]*len(nums)
        counter = 0
        
        # add numbers less than pivot to res
        for n in nums:
            if n < pivot:
                res[counter] = n
                counter += 1
        
        # add numbers equal to pivot to res
        for n in nums:
            if n == pivot:
                res[counter] = n
                counter += 1
        
        # add numbers greater than pivot to res
        for n in nums:
            if n > pivot:
                res[counter] = n
                counter += 1
                            
        # return nums after the rearrangement
        return res
        