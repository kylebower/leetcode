class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming = 0
        while x > 0 or y > 0:
            cur_x = x%2
            cur_y = y%2
            if cur_x != cur_y:
                hamming += 1
            x //= 2
            y //= 2
        return hamming
    