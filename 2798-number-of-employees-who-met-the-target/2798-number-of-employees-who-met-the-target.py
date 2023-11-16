class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # define count of Number of Employees Who Met the Target
        num_employees = 0
        
        # iterate through hours to count Number of Employees Who Met the Target
        for h in hours:
            if h>=target:
                num_employees += 1
        
        # return result
        return num_employees
    
    # time complexity: O(n)
    # space complexity: O(1)
    