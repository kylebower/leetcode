class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        res = 0
        paired = set()
        for i in range(n-1):
            for j in range(i+1,n):
                if words[i] == words[j][::-1] and i not in paired and j not in paired:
                    res += 1
                    paired.add(i)
                    paired.add(j)
        return res
    