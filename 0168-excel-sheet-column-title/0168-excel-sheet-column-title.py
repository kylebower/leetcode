class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = ''
        
        if columnNumber <= 26:
            return chr(ord('A') + columnNumber - 1)
        else:
            while columnNumber > 0:
                (columnNumber,r) = divmod(columnNumber, 26)
                if r == 0:
                    columnNumber -= 1
                    r += 26
                res += chr(ord('A') + r - 1)
        
        return res[::-1]
    