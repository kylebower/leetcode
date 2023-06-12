class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = list(set(arr))
        temp.sort()
        
        d = {}
        for i, elem in enumerate(temp):
            d[elem] = i+1
        
        return [d[elem] for elem in arr]
    
    # time complexity: O(n*log(n))
    # space complexity: O(n)
    