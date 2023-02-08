class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([y for _,y in sorted(zip(indices, s))])