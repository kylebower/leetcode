class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        n = len(letters)
        
        # define pointers
        L, R = 0, n-1
        
        # perform binary search
        while L + 1 < R:
            mid = int(L + (R-L)/2)
            if target < letters[mid]:
                R = mid
            else:
                L = mid
        
        # return smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters
        if letters[L] > target:
            result = letters[L]
        elif letters[R] > target:
            result = letters[R]
        else:
            result = letters[0]
        return result