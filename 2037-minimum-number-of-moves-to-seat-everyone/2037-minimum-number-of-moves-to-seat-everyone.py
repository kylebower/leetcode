class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        
        num_moves = 0
        for i in range(len(seats)):
            num_moves += abs(seats[i]-students[i])
        
        return num_moves
    