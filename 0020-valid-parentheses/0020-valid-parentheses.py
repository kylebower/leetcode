class Solution:
    def isValid(self, s: str) -> bool:
        # FILO - use stack
        
        stack = []
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            else: # c in set(')', '}', ']')
                if stack == []:
                    return False
                else:
                    top = stack[-1]
                
                valid = (c == ')' and top == '(') or (c == '}' and top == '{') or (c == ']' and top == '[')
                if valid:
                    stack.pop()
                else:
                    return False
        return stack == []
    