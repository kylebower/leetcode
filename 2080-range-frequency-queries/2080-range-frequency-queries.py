class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        # Use dictionary to store for each value, the indices where that value appeared
        self.d = defaultdict(list)
        for i, a in enumerate(arr):
            self.d[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:        
        
        # return 0 if value not in arr
        if value not in list(self.d.keys()):
            return 0
        
        occurrences = self.d[value]
        
        # first = self.binarySearch(occurences, left, right)
        
        # binary search to find first occurence of value
        first = 0
        l = 0
        r = len(occurrences)-1
        while l+1 < r:
            mid = int(l + (r-l)/2)
            if occurrences[mid] <= left:
                l = mid
            else:
                r = mid
        if occurrences[l] >= left:
            first = l
        elif occurrences[r] >= left:
            first = r
        else:
            return 0
            
        # binary search to find last occurence of value
        last = 0
        l = 0
        r = len(occurrences)-1
        while l+1 < r:
            mid = int(l + (r-l)/2)
            if occurrences[mid] >= right:
                r = mid
            else:
                l = mid
        if occurrences[r] <= right:
            last = r
        elif occurrences[l] <= right:
            last = l
        else:
            return 0
        
        return last - first + 1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)