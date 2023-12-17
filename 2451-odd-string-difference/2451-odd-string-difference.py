class Solution:
    def oddString(self, words: List[str]) -> str:
        differences = []
        n = len(words[0])
        m = len(words)
        for i, w in enumerate(words):
            diff = [0]*(n-1)
            for j in range(n-1):
                diff[j] = ord(w[j+1]) - ord(w[j])
            differences.append(diff)
        for i, dif in enumerate(differences):
            if dif != differences[(i+1)%m] and dif != differences[(i-1)%m]:
                return words[i]
        return '0'