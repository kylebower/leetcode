class Solution:
    def totalMoney(self, n: int) -> int:
        savings = 0
        next_deposit = 1
        for day in range(n):
            savings += next_deposit
            next_deposit += 1
            if day%7 == 6:
                next_deposit -= 6
        return savings