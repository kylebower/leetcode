class Solution:
    def isValid(self, s: str) -> bool:
        # FILO - use stack
        
        stack = []
        d = {'(': ')', '{':'}', '[':']'}
        for c in s:
            if c in d:
                stack.append(c)
            else: # c in set(')', '}', ']')
                if stack == []:
                    return False
                
                if d[stack.pop()] != c:
                    return False
                
        return stack == []
    