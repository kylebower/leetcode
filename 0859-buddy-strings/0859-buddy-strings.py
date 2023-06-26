class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # return False if different lengths
        if len(s) != len(goal):
            return False
        
        # if string equal return true if they share a repeated letter
        if s == goal and len(set(s)) < len(s):
            return True
        
        # return true if you can swap two letters in s so the result is equal to goal, else false
        diff = [[a,b] for (a,b) in zip(s,goal) if a!=b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]
    