class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        # define array for number of users whose UAM equals j
        answer = [0]*k
        
        # define dict d[ID] = set of times when they performed an action
        d = {}
        for val in logs:
            if val[0] in d:
                set_v0 = d[val[0]]
                set_v0.add(val[1])
                d[val[0]] = set_v0
            else:
                d[val[0]] = {val[1]}
        
        # define dict d2[ID] = UAM
        d2 = {}
        for val in logs:
            d2[val[0]] = len(list(d.get(val[0])))
        
        # update array answer
        for j in list(d2.values()):
            answer[j-1] += 1
        
        # return array
        return answer
    