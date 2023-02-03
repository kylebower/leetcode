class Solution:
    def minimumSum(self, num: int) -> int:
        # create array of digits in num
        num_array = [int(x) for x in str(num)]
        
        # sort digits
        num_array.sort()
        
        # find minimum possible sum of new1 and new2
        new1 = 10*num_array[0] + num_array[2]
        new2 = 10*num_array[1] + num_array[3]
        
        # Return the minimum possible sum of new1 and new2
        return new1 + new2        
        
    # time complexity: O(1)
    # space complexity: O(1)
