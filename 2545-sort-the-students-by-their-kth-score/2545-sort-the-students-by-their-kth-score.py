class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        # define array of kth score
        n = len(score[0])   # n exams
        m = len(score)      # m students
        kth = [0]*m
        for i in range(m):
            kth[i] = score[i][k]
        
        # sort students by kth score
        sorted_score = [y for _,y in sorted(zip(kth,score))]
        
        # return sorted matrix
        return sorted_score[::-1]
    