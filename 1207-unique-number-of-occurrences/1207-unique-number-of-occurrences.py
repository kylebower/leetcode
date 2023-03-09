class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # make dict of number of occurrences of each value in arr
        arr_dict = {}
        for n in arr:
            arr_dict[n] = arr_dict.get(n,0) + 1
        
        # return true if the number of occurrences of each value in the array is unique or false otherwise
        set_num_occ = set()
        for value in list(arr_dict.values()):
            if value in set_num_occ:
                return False
            else:
                set_num_occ.add(value)
        
        return True
    