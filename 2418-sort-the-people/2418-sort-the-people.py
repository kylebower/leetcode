class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [y for x,y in sorted(zip(heights,names))][::-1]