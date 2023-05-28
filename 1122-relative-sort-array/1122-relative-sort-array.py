class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        # sort arr1 in ascending order
        arr1.sort()
        
        # sort array
        for n in arr2:
            arr1.sort(key = lambda x: x==n)
        
        # find index of first element in arr1 that is in arr2
        index = 0
        while arr1[index] != arr2[0]:
            index += 1
        
        # return sorted array
        return arr1[index:] + arr1[:index]
        