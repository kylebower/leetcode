class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort arr
        arr.sort()
        
        # find min abs diff
        diff = arr[-1] - arr[0]
        n = len(arr)
        for i in range(n-1):
            cur_diff = arr[i+1] - arr[i]
            diff = min(diff, cur_diff)
        
        # create list of pairs
        res = []
        L = 0
        R = 1
        while R < n and L < n:
            if arr[R] - arr[L] < diff:
                R += 1
            elif arr[R] - arr[L] == diff:
                res.append([arr[L],arr[R]])
                L += 1
                R += 1
            else:
                L += 1
        
        # return list of pairs
        return res
    