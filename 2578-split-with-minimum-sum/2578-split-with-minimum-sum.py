class Solution:
    def splitNum(self, num: int) -> int:
        
        # create list of char in str(num)
        num_list = list(str(num))
        # sort list
        num_list.sort()
        # create string from sorted list
        num_str = ''.join(num_list)
        
        # find strings for num1 and num2
        num1_str = num_str[::2]
        num2_str = num_str[1::2]
        
        # define result
        result = int(num1_str) + int(num2_str)
        
        # return result
        return result
    