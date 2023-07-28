class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        kbeauty = 0
        for i in range(len(str(num))-k+1):
            if int(str(num)[i:i+k]) != 0 and num % int(str(num)[i:i+k]) == 0:
                kbeauty += 1
        return kbeauty
    