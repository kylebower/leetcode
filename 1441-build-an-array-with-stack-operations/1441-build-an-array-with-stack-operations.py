class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        stk = []
        
        ti = 0
        
        for i in range(1,n+1):
            stk.append(i)
            output.append("Push")
            if stk == target:
                return output
            if target[ti] != i:
                stk.pop()
                output.append("Pop")
            else:
                ti += 1
            