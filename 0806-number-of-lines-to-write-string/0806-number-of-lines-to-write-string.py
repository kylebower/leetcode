class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        nlines = 1
        wline = 0
        
        for c in s:
            w = widths[ord(c) - ord('a')]
            if w + wline > 100:
                nlines += 1
                wline = w
            else:
                wline += w
        
        return [nlines, wline]
    
    # time complexity: O(n)
    # space complexity: O(1)
    