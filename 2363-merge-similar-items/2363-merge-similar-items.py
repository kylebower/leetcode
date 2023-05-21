class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for item in items1:
            d[item[0]] = d.get(item[0],0)+item[1]
        for item in items2:
            d[item[0]] = d.get(item[0],0)+item[1]
        ret = [[x,d[x]] for x in d]
        ret.sort()
        return ret