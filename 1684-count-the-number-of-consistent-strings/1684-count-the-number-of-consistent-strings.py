class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        d = {}
        for c in allowed:
            d[c] = 1
        
        n_words = len(words)
        n_inconsistent = 0
        
        for w in words:
            print(w)
            for c in w:
                print(c)
                if c not in d:
                    n_inconsistent += 1
                    break
                    
        return n_words - n_inconsistent 
       