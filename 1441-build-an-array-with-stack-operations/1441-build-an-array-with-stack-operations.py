class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        ti = 0
        
        for i in range(1,n+1):
            output.append("Push")
            if target[-1] == i:
                return output
            elif target[ti] != i:
                output.append("Pop")
            else:
                ti += 1
            