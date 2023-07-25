class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # define count of passengers who are strictly more than 60 years old
        count = 0
        
        # iterate for each person check if they are >60
        for person in details:
            age = int(person[11:13])
            # increment count if person is >60
            if age > 60:
                count += 1
                
        # Return the number of passengers who are strictly more than 60 years old
        return count
    
    # time complexity: O(n)
    # space complexity: O(1)
    