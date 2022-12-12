class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:       
        for x in ransomNote:
            location_x = magazine.find(x)
            if location_x == -1:
                return False
            else:
                magazine = magazine[:location_x] + magazine[location_x+1:]
        return True