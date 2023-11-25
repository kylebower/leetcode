class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        try:
            for sandwhich in sandwiches:
                students.remove(sandwhich)
        except:
            pass
        return len(students)