class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        while amount != [0]*3:
            amount.sort()
            amount[2] -= 1
            if amount[1] > 0:
                amount[1] -= 1
            res += 1
        return res
    