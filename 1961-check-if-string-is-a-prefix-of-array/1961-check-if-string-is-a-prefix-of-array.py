class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        cur = ''
        for k in range(len(words)):
            cur += words[k]
            if s == cur:
                return True
        return False
    