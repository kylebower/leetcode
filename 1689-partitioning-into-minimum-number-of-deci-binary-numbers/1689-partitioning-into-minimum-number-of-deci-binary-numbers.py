class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0
        n_len = len(n)
        for i in range(n_len):
            i_int = int(n[i])
            result = max(result,i_int)
        # return the minimum number of positive deci-binary numbers needed so that they sum up to n
        return result
