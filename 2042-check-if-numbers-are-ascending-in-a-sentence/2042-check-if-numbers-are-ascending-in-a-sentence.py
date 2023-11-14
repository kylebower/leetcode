class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(" ")
        numbers = [int(w) for w in words if w.isnumeric()]
        for i in range(len(numbers)-1):
            if numbers[i+1] <= numbers[i]:
                return False
        return True
    