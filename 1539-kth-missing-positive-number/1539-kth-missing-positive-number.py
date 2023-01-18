class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur = 1
        i = 1
        for i in range(len(arr)):
            while cur != arr[i]:
                k -= 1
                if k == 0:
                    return cur
                cur += 1
            cur += 1
        return cur + k - 1
            