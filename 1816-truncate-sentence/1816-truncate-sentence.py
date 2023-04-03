class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s_array = s.split(' ')
        s_array_trunc = s_array[:k]
        s_trunc = ' '.join(s_array_trunc)
        return s_trunc
    