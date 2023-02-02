class Solution:
    def maximum69Number (self, num: int) -> int:
        array_num = [int(x) for x in str(num)]
        for i, d in enumerate(array_num):
            if d == 6:
                array_num[i] = 9
                break
        res = 0
        for d in array_num:
            res = 10*res + d
        return res