class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = len(startTime)
        
        # iterate to count number of students doing their homework at time queryTime
        res = 0
        for i in range(n):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                res += 1
                
        # Return the number of students doing their homework at time queryTime
        return res
    
    # time complexity: O(n)
    # space complexity: O(1)
    