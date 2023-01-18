class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersect = set(nums[0])
        for i in range(1,len(nums)):
            intersect = intersect & set(nums[i])
        list_intersect = list(intersect)
        list_intersect.sort()
        return list_intersect
        