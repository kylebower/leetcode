class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDictionary = {}
        for c in magazine:
            magazineDictionary[c] = magazineDictionary.get(c,0)+1
        
        for c in ransomNote:
            magazineDictionary[c] = magazineDictionary.get(c,0)-1
            if magazineDictionary[c] < 0:
                return False
            
        return True