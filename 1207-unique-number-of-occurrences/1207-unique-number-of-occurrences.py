class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # make dict of number of occurrences of each value in arr
        arr_dict = {}
        for n in arr:
            arr_dict[n] = arr_dict.get(n,0) + 1
        
        # return true if the number of occurrences of each value in the array is unique or false otherwise
        return len(list(arr_dict.values())) == len(set(arr_dict.values()))
    