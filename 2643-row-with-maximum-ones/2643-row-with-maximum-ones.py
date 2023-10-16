class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ind = 0
        max_count = 0
        for i, row in enumerate(mat):
            row_count = sum(row)
            if row_count > max_count:
                max_count = row_count
                max_ind = i
        return [max_ind, max_count]
                