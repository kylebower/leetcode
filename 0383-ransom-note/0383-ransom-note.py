class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDictionary = {}
        for i in range(len(magazine)):
            c = magazine[i]
            c_count = magazineDictionary.get(c, 0)
            magazineDictionary[c] = c_count + 1
        
        for i in range(len(ransomNote)):
            c = ransomNote[i]
            c_count = magazineDictionary.get(c, 0)
            if c_count <= 0:
                return False
            magazineDictionary[c] = c_count - 1
            
        return True