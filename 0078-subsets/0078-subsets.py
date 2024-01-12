class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for k in range(2**n):
            listj = []
            binaryk = list(str(bin(k)))[2:]
            binaryk.reverse()
            for i, num in enumerate(nums):
                if binaryk[i] == '1':
                    listj.append(i)
                if i == len(binaryk)-1:
                    break
            res.append([nums[j] for j in listj])
        return res
    