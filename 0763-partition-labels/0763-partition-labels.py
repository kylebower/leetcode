class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer = []
        n = len(s)
        # Base case
        if n < 2:
            answer = [1]
            return answer
        
        # make dictionary of last appearences of each letter in string
        dict = {}
        for i in range(n):
            dict.update({s[i]:i})
        
        # define pointers
        L = 0
        R = 0
        curr_max = dict[s[L]]
        
        # iterate to find partitions
        while R < n:
            R_max = dict[s[R]]
            if R_max > curr_max:
                curr_max = R_max
            if R == curr_max:
                answer.append(R+1-L)
                L = R+1
            R += 1
        
        # Return a list of integers representing the size of these partitions
        return answer
